Readme- Summary Extraction with BERT


This script utilizes BERT-based sentence embeddings to extract summaries from CSV files containing dialogues or text data. It employs the Hugging Face 'transformers' library for BERT models, 'pandas' for data manipulation, and 'scikit-learn' for clustering.


 Prerequisites
Make sure you have the required libraries installed. You can install them using the following command:
'''bash
pip install -r requirements.txt
'''


 Usage
1. Clone the repository:
'''bash
git clone <repository-url>
cd <repository-directory>
'''
2. Install dependencies:
'''bash
pip install -r requirements.txt
'''
3. Run the script:
'''bash
python your_script_name.py
'''
4. The script will process each CSV file and generate a summary, saving the results to a CSV file named 'summaries.csv'.
 Configuration
- 'your_script_name.py': Main script for extracting summaries from CSV files.
- 'requirements.txt': List of required Python packages.
- 's4e01.csv', 's4e02.csv', ..., 's5e16.csv': Sample CSV files with dialogues or text data for each episode.
- 'summaries.csv': CSV file containing the extracted summaries.


 Customization


- Adjust the 'model_name' variable to use a different BERT model.
- Modify the list of 'csv_file_paths' to include the CSV files you want to process.


 Acknowledgments


- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)