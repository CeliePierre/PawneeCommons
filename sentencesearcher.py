import pandas as pd
from sentence_transformers import SentenceTransformer, util
import gui


class SentenceSearcher:
    def __init__(self, query):
        self.model = SentenceTransformer('roberta-base-nli-mean-tokens')
        self.QUERY_RESULTS = ''
        self.query = query

    def set_query_results(self, query_results_in):
        self.QUERY_RESULTS = query_results_in

    def get_query_results(self):
        return self.QUERY_RESULTS

    def load_vectors(self, file_path):
        return pd.read_csv(file_path).values.tolist()

    def search(self, sentences_embeddings, original_sentences, file_names, query, top_k):
        query_embedding = self.model.encode([query])
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

    def start_search(self):
        conn = gui.get_database_connection()
        get_mysql_sentences = gui.get_table(conn, 'transcripts')
        mysql_sentences = [row.get('dialogue') for row in get_mysql_sentences]
        mqsql_IDs = [row.get('lID') for row in get_mysql_sentences]

        # Load vectors from the file
        vectors = self.load_vectors('vectors.csv')

        # Ensure the question is not empty
        if self.query.strip():
            search_results = self.search(vectors, mysql_sentences, mqsql_IDs, self.query, 5)
            for result in search_results:
                self.QUERY_RESULTS += "Line ID: {}\nDialogue: {}\nScore: {:.4f}\n\n".format(result['file_name'],
                                                                                            result['sentence'],
                                                                                            result['score'])
        else:
            self.QUERY_RESULTS = "Please enter a valid question."

        self.set_query_results(self.QUERY_RESULTS)
