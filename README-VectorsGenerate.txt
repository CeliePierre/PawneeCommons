Readme-VectorsGenerate


This script performs sentence embedding and allows you to search for similar sentences within a collection. It utilizes the [Sentence Transformers](https://www.sbert.net/) library for creating embeddings.
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
4. Enter a sentence when prompted to search for similar sentences within the collection.


 File Structure


- 'your_script_name.py': Main script for generating sentence vectors and performing searches.
- 'requirements.txt': List of required Python packages.
- 'vectors.csv': CSV file containing the generated sentence vectors.
- 's1e01.csv', 's1e02.csv', ..., 's7e12.csv': Sample CSV files with sentences for each episode.


 Acknowledgments


- [Sentence Transformers](https://www.sbert.net/)
- [Pandas](https://pandas.pydata.org/)