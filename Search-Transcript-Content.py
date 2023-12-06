# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1srexN8iEWcRULeAyozMY7u4kzrqJ2afh
"""

import pandas as pd
from sentence_transformers import SentenceTransformer, util

def load_data(file_paths, column_name):
    all_sentences = []
    file_names = []
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        sentences = df[column_name].tolist()
        all_sentences.extend(sentences)
        file_names.extend([file_path] * len(sentences))
    return all_sentences, file_names

def load_vectors(file_path):
    return pd.read_csv(file_path).values.tolist()

def search(sentences_embeddings, original_sentences, file_names, query, model, top_k):
    query_embedding = model.encode([query])
    cosine_scores = util.cos_sim(query_embedding, sentences_embeddings)[0]
    pairs = [{'index': i, 'score': cosine_scores[i]} for i in range(len(cosine_scores))]
    pairs = sorted(pairs, key=lambda x: x['score'], reverse=True)

    results = []
    for pair in pairs[:top_k]:
        index = pair['index']
        sentence = original_sentences[index]
        file_name = file_names[index]
        score = pair['score']
        results.append({'sentence': sentence, 'file_name': file_name, 'score': score})

    return results

def main():
    model = SentenceTransformer('roberta-base-nli-mean-tokens')

    # Read original sentences and file names from multiple CSV files
    csv_file_paths = ['s1e01.csv', 's1e02.csv', 's1e03.csv', 's1e04.csv', 's1e05.csv', 's1e06.csv',
                      's2e01.csv', 's2e02.csv', 's2e03.csv', 's2e04.csv', 's2e05.csv', 's2e06.csv',
                      's2e07.csv', 's2e08.csv', 's2e09.csv', 's2e10.csv', 's2e11.csv', 's2e12.csv',
                      's2e13.csv', 's2e14.csv', 's2e15.csv', 's2e16.csv', 's2e17.csv', 's2e18.csv',
                      's2e19.csv', 's2e20.csv', 's2e21.csv', 's2e22.csv', 's2e23.csv', 's2e24.csv',
                      's3e01.csv', 's3e02.csv', 's3e03.csv', 's3e04.csv', 's3e05.csv', 's3e06.csv',
                      's3e07.csv', 's3e08.csv', 's3e09.csv', 's3e10.csv', 's3e11.csv', 's3e12.csv',
                      's3e13.csv', 's3e14.csv', 's3e15.csv', 's3e16.csv',
                      's4e01.csv', 's4e02.csv', 's4e03.csv', 's4e04.csv', 's4e05.csv', 's4e06.csv',
                      's4e07.csv', 's4e08.csv', 's4e09.csv', 's4e10.csv', 's4e11.csv', 's4e12.csv',
                      's4e13.csv', 's4e14.csv', 's4e15.csv', 's4e16.csv', 's4e17.csv', 's4e18.csv',
                      's4e19.csv', 's4e20.csv', 's4e21.csv', 's4e22.csv',
                      's5e01.csv', 's5e02.csv', 's5e03.csv', 's5e04.csv', 's5e05.csv', 's5e06.csv',
                      's5e07.csv', 's5e08.csv', 's5e09.csv', 's5e10.csv', 's5e11.csv', 's5e12.csv',
                      's5e13.csv', 's5e14.csv', 's5e15.csv', 's5e16.csv', 's5e17.csv', 's5e18.csv',
                      's5e19.csv', 's5e20.csv', 's5e21.csv', 's5e22.csv',
                      's6e01.csv', 's6e02.csv', 's6e03.csv', 's6e04.csv', 's6e05.csv', 's6e06.csv',
                      's6e07.csv', 's6e08.csv', 's6e09.csv', 's6e10.csv', 's6e11.csv', 's6e12.csv',
                      's6e13.csv', 's6e14.csv', 's6e15.csv', 's6e16.csv', 's6e17.csv', 's6e18.csv',
                      's6e19.csv', 's6e20.csv',
                      's7e01.csv', 's7e02.csv', 's7e03.csv', 's7e04.csv', 's7e05.csv', 's7e06.csv',
                      's7e07.csv', 's7e08.csv', 's7e09.csv', 's7e10.csv', 's7e11.csv', 's7e12.csv']

    column_name = 'Line'
    original_sentences, file_names = load_data(csv_file_paths, column_name)

    # Load vectors from the file
    vectors = load_vectors('vectors.csv')

    # Prompt user for a question
    query = input("Search for Similar Sentences< Please Enter your sentence>:")
    print("\n----------------------\n")

    # Ensure the question is not empty
    if query.strip():
        search_results = search(vectors, original_sentences, file_names, query, model, 5)
        for result in search_results:
            print("File: {}\nSentence: {}\nScore: {:.4f}\n".format(result['file_name'], result['sentence'], result['score']))
    else:
        print("Please enter a valid question.")

if __name__ == '__main__':
    main()