README-GUI: 


Pawnee Commons: TV Show Database


 Introduction
Welcome to Pawnee Commons, a TV show database for fans and creators. This Python application uses PySimpleGUI for the graphical user interface and connects to a MySQL database to provide information about episodes, transcripts, characters, and more.


 Getting Started
Before running the code, make sure to set up a MySQL database and update the 'config.json' file with your database connection details.


'''json
{
  "mysql": {
    "host": "your_host",
    "user": "your_username",
    "password": "your_password",
    "database": "your_database"
  }
}
'''


 Features
1. Browse Section
   - Browse Episodes
   - Browse Transcripts
   - Browse Characters
   - Browse Cast & Crew


2. Fun Facts Section
   - Best Seasons
   - Best Episodes
   - Main Cast
   - Guest Stars
   - Most Lines
   - Popular Characters
   - Actors and Creators


3. Search Section
   - Search Characters
   - Search Episodes
   - Search Cast & Crew
   - Search Transcripts
   - Search Viewers


4. Additional Functionality
   - Click on items in the tables to view detailed information.
   - Search and filter data based on various criteria.


 How to Use
1. Run the script, and the main window will appear.
2. Use the tabs to navigate between different sections.
3. Explore the browse, search, and fun facts features.
4. Click on items in tables to view more details.
5. Customize and extend the code for your specific needs.


 Notes
- The code uses PySimpleGUI for the GUI and connects to a MySQL database for data retrieval.
- Make sure to have the required Python packages installed ('mysql.connector', 'PySimpleGUI').


 Authors
- Célie Pierre
- Sarah Lawrence
- Reihaneh Maarefdoust


 Acknowledgments
This project was developed as part of the COS 457 Database Systems course at the University of Southern Maine in the fall of 2023.


Feel free to reach out for any questions or feedback!


 
________________
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


 
________________
README: Database Character Management


This Python script provides functionality for managing character information in a MySQL database. It includes features for adding new character names, checking if a name already exists, and retrieving information about a character from the database.


 Prerequisites


Before running the script, ensure you have the following:


1. MySQL server installed and running.
2. Python installed on your machine.
3. Required Python libraries:


'''bash
pip install mysql-connector-python
'''


 Configuration


The script uses a configuration file ('config.json') to connect to the MySQL database. Make sure to create this file in the same directory as the script with the following structure:


'''json
{
  "mysql": {
    "host": "your_host",
    "user": "your_user",
    "password": "your_password",
    "database": "your_database"
  }
}
'''


Replace '"your_host"', '"your_user"', '"your_password"', and '"your_database"' with your MySQL server details.


 Usage


1. Run the script:


'''bash
python script_name.py
'''


Replace 'script_name.py' with the actual name of your Python script.


2. The script will prompt you if you want to add a new character name. Enter "yes" to add a new name or "no" to exit.


3. If adding a new name, provide the character's first and last names.


4. The script will check if the name already exists in the database. If it does, an error message will be displayed, and the changes will be rolled back. If not, the new name will be added.


5. Optionally, you can choose to check where the name is in the database. Enter "yes" to check or "no" to continue without checking.


6. The script will continue prompting you until you enter "no" when asked if you want to add a new name.


 Example


'''bash
python character_management.py
'''


Follow the on-screen prompts to add or check character names in the database.


 Important Notes


- Ensure that the MySQL server is running and the configuration file ('config.json') is properly set up.
- The script uses a 'charactr' table in the database, so make sure this table exists with the appropriate schema:


'''sql
CREATE TABLE charactr (
    cID INT AUTO_INCREMENT PRIMARY KEY,
    cFirstName VARCHAR(255),
    cLastName VARCHAR(255)
);
'''


Feel free to customize the script according to your specific database schema and requirements.
'''