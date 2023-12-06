README- Search Transcripts content


This Python script performs a semantic search on a collection of sentences using sentence embeddings. It utilizes the Sentence Transformers library and a pre-trained model (roberta-base-nli-mean-tokens) to encode sentences into vectors.


Overview


The script consists of the following main functions:


- load_data: Reads sentences and file names from multiple CSV files.
- load_vectors: Loads sentence vectors from a CSV file.
- search: Performs a semantic search based on user input query and displays the top matching sentences.


Usage


1. Install the required libraries:


    ```bash
    pip install pandas sentence-transformers
    ```


2. Run the script:


    ```bash
    python script_name.py
    ```


3. Enter a sentence when prompted, and the script will return the top matching sentences along with their scores.


'' Dependencies


- pandas
- sentence-transformers


'' Files


- `script_name.py`: The main Python script.
- `vectors.csv`: CSV file containing pre-computed sentence vectors.
- `s1e01.csv`, `s1e02.csv`, ...: CSV files containing original sentences.


'' Configuration


The script uses the 'roberta-base-nli-mean-tokens' model by default. You can modify the model in the `main` function if needed.


'' Example


```bash
Search for Similar Sentences: Please enter your sentence here.


----------------------


File: s1e01.csv
Sentence: Example sentence from episode 1.
Score: 0.9213


File: s2e05.csv
Sentence: Another example sentence from episode 5.
Score: 0.8902