# Copyright (c) Linyuan Gong
# Licensed under the MIT license.

# -*- coding:utf-8 -*-
import os
from typing import List, Set

import bleu
import code_bleu.build
import code_bleu.dataflow_match
import code_bleu.syntax_match
import code_bleu.weighted_ngram_match


def make_weights(reference_tokens: List[str], key_word_set: Set[str]):
    return {
        token: 1 if token in key_word_set else 0.2
        for token in reference_tokens
    }


def calc_code_bleu(refs: List[str], hyp: str, lang: str, params=(0.25, 0.25, 0.25, 0.25)):
    code_bleu.build.maybe_build()

    alpha, beta, gamma, theta = params
    assert abs(alpha + beta + gamma + theta - 1) < 1e-8
    refs = [ref.strip() for ref in refs]
    hyp = hyp.strip()

    tokenized_refs = [ref.split() for ref in refs]
    tokenized_hyp = hyp.split()
    ngram_match_score = bleu.sentence_bleu(tokenized_refs, tokenized_hyp)

    keywords_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keywords', lang + ".txt")
    with open(keywords_file, "r", encoding="utf-8") as f:
        keywords = set([x.strip() for x in f.readlines()])
    tokenized_refs_with_weights = [
        [ref, make_weights(ref, keywords)]
        for ref in tokenized_refs
    ]
    weighted_ngram_match_score = code_bleu.weighted_ngram_match.sentence_bleu(
        tokenized_refs_with_weights,
        tokenized_hyp
        )

    syntax_match_score = code_bleu.syntax_match.corpus_syntax_match([refs], [hyp], lang)

    dataflow_match_score = code_bleu.dataflow_match.corpus_dataflow_match([refs], [hyp], lang)

    return (
        alpha * ngram_match_score
        + beta * weighted_ngram_match_score
        + gamma * syntax_match_score
        + theta * dataflow_match_score
    )
