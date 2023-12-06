README: Sentence Searcher


The Sentence Searcher is a Python script designed for searching through a database of transcripts using semantic similarity. It employs the SentenceTransformer library to encode sentences into vectors and then calculates the cosine similarity between a user query and the stored sentences. This tool is particularly useful for finding similar lines or dialogues in a collection of transcripts.


 Prerequisites


Make sure you have the necessary Python libraries installed. You can install them using the following commands:


'''bash
pip install pandas
pip install sentence-transformers
pip install PySimpleGUI
'''


 Usage


To use the Sentence Searcher, follow these steps:


1. Import the required libraries:


'''python
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import gui
'''


2. Create an instance of the 'SentenceSearcher' class, providing a query string:


'''python
searcher = SentenceSearcher("Your query goes here.")
'''


3. Load the vectors from a file using the 'load_vectors' method:


'''python
vectors = searcher.load_vectors('vectors.csv')
'''


4. Start the search using the 'start_search' method:


'''python
searcher.start_search()
'''


5. Retrieve the results using the 'get_query_results' method:


'''python
results = searcher.get_query_results()
print(results)
'''


 Important Notes


- Ensure that you have a valid database connection before starting the search. The 'get_database_connection' function from the 'gui' module is used for this purpose.


- The search results include the Line ID, Dialogue, and Score for each match.


- The vectors file ('vectors.csv') should contain pre-computed sentence embeddings.


- Make sure to replace "Your query goes here." with the actual query you want to search for.


 Example


'''python
 Example Usage
searcher = SentenceSearcher("Ron Swanson")
vectors = searcher.load_vectors('vectors.csv')
searcher.start_search()
results = searcher.get_query_results()
print(results)
'''


This will perform a semantic search for lines similar to "Ron Swanson" in the transcripts and display the results including Line ID, Dialogue, and Score.


Feel free to customize the code according to your specific use case.