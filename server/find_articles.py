import numpy as np
import pandas as pd
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


def preprocess_text(text):
    stop_words = np.array(stopwords.words('english'))
    
    text = text.lower().replace('-', ' ')
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d', '', text)
    
    text = word_tokenize(text)
    ps = PorterStemmer()
    processed_text = []
    for word in text:
        if word not in stop_words:
            processed_text += [ps.stem(word)]

    return np.array(processed_text)


def low_rank_approx(matrix, r):
    u, s, v = np.linalg.svd(matrix, full_matrices=False)
    approx_matrix = np.zeros((len(u), len(v)))
    for i in range(r):
        approx_matrix += s[i] * np.outer(u.T[i], v[i])
    return approx_matrix


def search(words, bow, text):
    text = preprocess_text(text)
    text_vector = np.zeros((len(words), 1), dtype=float)
    for word in text:
        if word in words:
            text_vector[np.where(words == word)[0][0], 0] += 1/len(text)
    text_norm = np.linalg.norm(text_vector)

    theta_values = []
    for index, document in enumerate(bow.T):
        theta_values += [((text_vector.T @ document) / (text_norm * np.linalg.norm(document)), index)]
    theta_values.sort(key=lambda x: x[0], reverse=True)
    
    indexes = []
    for value, index in theta_values[:10]:
        indexes += [index]
    
    return indexes


def search_normalized(words, bow, text):
    text = preprocess_text(text)
    text_vector = np.zeros((len(words), 1), dtype=float)
    for word in text:
        if word in words:
            text_vector[np.where(words == word)[0][0], 0] += 1/len(text)
    text_norm = np.linalg.norm(text_vector)

    theta_values = []
    for index, document in enumerate(bow.T):
        q = text_vector / text_norm
        d = document / np.linalg.norm(document)
        theta_values += [(q.T @ d, index)]
    theta_values.sort(key=lambda x: x[0], reverse=True)
    
    indexes = []
    for value, index in theta_values[:10]:
        indexes += [index]
    
    return indexes


def get_articles(indexes):
    df = pd.read_csv('./data/bbc-news-data.csv', sep='\t')
    result = df.iloc[indexes]
    return result.to_json(orient='records')


def main(text):
    words = np.load('./data/words.npy')
    bow = np.load('./data/bow.npy')
    indexes = search_normalized(words, bow, text)
    return get_articles(indexes)
