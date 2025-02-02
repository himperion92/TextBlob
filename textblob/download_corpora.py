#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Downloads the necessary NLTK corpora for TextBlob.

Usage: ::

    $ python -m textblob.download_corpora

If you only intend to use TextBlob's default models, you can use the "lite"
option: ::

    $ python -m textblob.download_corpora lite

"""
import os
import sys
import nltk

MIN_CORPORA = [
    'brown',  # Required for FastNPExtractor
    'punkt',  # Required for WordTokenizer
    'wordnet',  # Required for lemmatization
    'averaged_perceptron_tagger',  # Required for NLTKTagger
]

ADDITIONAL_CORPORA = [
    'conll2000',  # Required for ConllExtractor
    'movie_reviews',  # Required for NaiveBayesAnalyzer
]

ALL_CORPORA = MIN_CORPORA + ADDITIONAL_CORPORA


def download_lite(download_dir=None):
    for each in MIN_CORPORA:
        nltk.download(each, download_dir=download_dir)


def download_all(download_dir=None):
    for each in ALL_CORPORA:
        nltk.download(each, download_dir=download_dir)


def main():
    download_dir = os.getenv('NLTK_DATA')
    if 'lite' in sys.argv:
        download_lite(download_dir)
    else:
        download_all(download_dir)
    print("Finished.")


if __name__ == '__main__':
    main()
