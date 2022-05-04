import numpy as np
import pandas as pd
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


def get_df(path):
    return pd.read_csv(path, sep='\t')


def preprocess_article(article, stop_words, words):
    article = article.lower().replace('-', ' ')
    article = re.sub(r'[^\w\s]', '', article)
    article = re.sub(r'\d', '', article)
    
    article = word_tokenize(article)
    ps = PorterStemmer()
    processed_article = []
    for word in article:
        if word not in stop_words:
            processed_word = ps.stem(word)
            words.add(processed_word)
            processed_article += [processed_word]

    return np.array(processed_article)


def get_words(df):
    stop_words = np.array(stopwords.words('english'))
    words = set()

    for index, row in df.iterrows():
        row.content = preprocess_article(row.content, stop_words, words)
    
    words = np.array(list(words))
    return words


def create_bow(df, words):
    bow = np.zeros((len(words), len(df.index)), dtype=float)
    for index, row in df.iterrows():
        for word in row.content:
            bow[np.where(words == word)[0][0], index] += 1/len(row.content)
    return bow


def idf(words, bow):
    freq = np.zeros((len(words), 1))
    documents = len(bow.T)
    for i in range(len(words)):
        cnt = 0
        for document in bow.T:
            if document[i] > 0:
                cnt += 1
        freq[i] = np.log(documents/cnt)
    return bow * freq


def main():
    nltk.download('stopwords')
    nltk.download('punkt')

    df = get_df('./data/bbc-news-data.csv')
    print('Data frame loaded')
    words = get_words(df)
    print('Words set created')
    bow = create_bow(df, words)
    print('Bag of words created')
    bow = idf(words, bow)
    print('Inverse document frequency calculated')
    np.save('./data/words.npy', words)
    np.save('./data/bow.npy', bow)
