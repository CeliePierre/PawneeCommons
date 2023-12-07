
# README: Summary Extraction with BERT

This script utilizes BERT-based sentence embeddings to extract summaries from CSV files containing dialogues or text data. It employs the Hugging Face 'transformers' library for BERT models, 'pandas' for data manipulation, and 'scikit-learn' for clustering.

## Prerequisites
Make sure you have the required libraries installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python your_script_name.py
```

4. The script will process each CSV file and generate a summary, saving the results to a CSV file named 'summaries.csv'.

## Configuration
- 'your_script_name.py': Main script for extracting summaries from CSV files.
- 'requirements.txt': List of required Python packages.
- 's4e01.csv', 's4e02.csv', ..., 's5e16.csv': Sample CSV files with dialogues or text data for each episode.
- 'summaries.csv': CSV file containing the extracted summaries.

## Customization
- Adjust the 'model_name' variable to use a different BERT model.
- Modify the list of 'csv_file_paths' to include the CSV files you want to process.

## Acknowledgments
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)

# README: VectorsGenerate

This script performs sentence embedding and enables the search for similar sentences within a collection. It utilizes the [Sentence Transformers](https://www.sbert.net/) library for creating embeddings.

## Prerequisites
Ensure you have the required libraries installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python your_script_name.py
```

4. Enter a sentence when prompted to search for similar sentences within the collection.

## File Structure
- 'your_script_name.py': Main script for generating sentence vectors and performing searches.
- 'requirements.txt': List of required Python packages.
- 'vectors.csv': CSV file containing the generated sentence vectors.
- 's1e01.csv', 's1e02.csv', ..., 's7e12.csv': Sample CSV files with sentences for each episode.

## Acknowledgments
- [Sentence Transformers](https://www.sbert.net/)
- [Pandas](https://pandas.pydata.org/)

# README: Search Transcripts Content

This Python script performs a semantic search on a collection of sentences using sentence embeddings. It utilizes the Sentence Transformers library and a pre-trained model (roberta-base-nli-mean-tokens) to encode sentences into vectors.

## Overview
The script consists of the following main functions:
- `load_data`: Reads sentences and file names from multiple CSV files.
- `load_vectors`: Loads sentence vectors from a CSV file.
- `search`: Performs a semantic search based on user input query and displays the top matching sentences.

## Usage
1. Install the required libraries:

```bash
pip install pandas sentence-transformers
```

2. Run the script:

```bash
python script_name.py
```

3. Enter a sentence when prompted, and the script will return the top matching sentences along with their scores.

## Dependencies
- pandas
- sentence-transformers

## Files
- `script_name.py`: The main Python script.
- `vectors.csv`: CSV file containing pre-computed sentence vectors.
- `s1e01.csv`, `s1e02.csv`, ...: CSV files containing original sentences.

## Configuration
The script uses the 'roberta-base-nli-mean-tokens' model by default. You can modify the model in the `main` function if needed.

## Example
```bash
Search for Similar Sentences: Please enter your sentence here.

----------------------

File: s1e01.csv
Sentence: Example sentence from episode 1.
Score: 0.9213

File: s2e05.csv
Sentence: Another example sentence from episode 5.
Score: 0.8902
```
