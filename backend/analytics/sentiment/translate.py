# -*- coding: utf-8 -*-

from nltk import wordpunct_tokenize
from nltk.corpus import stopwords


def get_language_ratios(text):
    # Tokenize text
    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    # Calculate language ratios for each language in stopwords
    ratios = {}
    for language in stopwords.fileids():
        unique_stopwords = set(stopwords.words(language))
        unique_words = set(words)
        common = unique_words.intersection(unique_stopwords)
        ratios[language] = len(common)

    return ratios


def detect_language(text):
    # Return most likely language based on ratios
    ratios = get_language_ratios(text)
    language = max(ratios, key=ratios.get)

    return language
