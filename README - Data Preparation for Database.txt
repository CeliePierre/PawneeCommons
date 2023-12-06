Data Preparation for Database - README 


Viewers Data 
The code in this section combines information from two CSV files (`parks_and_rec_imdb.csv` and `parks_and_rec_episodes.csv`) related to the "Parks and Recreation" TV show. It specifically focuses on IMDb ratings, total votes, and US viewers data. 

Code Explanation: 

1. Data Source: The CSV files can be accessed on Kaggle: 
- IMDb Data: [Parks and Recreation IMDb Data] 
(https://www.kaggle.com/datasets/USERNAME/parks-and-recreation-imdb-data) - Episode Data: [Parks and Recreation Episodes Data] 
(https://www.kaggle.com/datasets/USERNAME/parks-and-recreation-episodes-data) 

2. Usage: 
- Replace the file paths (`imdb_csv_path` and `episode_data_csv_path`) with the actual paths to your downloaded CSV files. 
- Run the code to generate the `Viewers_data.csv` file. 



Episode Data 

This section extracts specific attributes from the `parks_and_rec_imdb.csv` file to create a new CSV file containing essential episode information. 
Code Explanation: 

1. Data Source: The IMDb CSV file can be accessed on Kaggle: [Parks and Recreation IMDb 
Data](https://www.kaggle.com/datasets/USERNAME/parks-and-recreation-imdb-data) 

2. Usage: 
- Replace the file path (`csv_file_path`) with the actual path to your downloaded IMDb CSV file. 
- Run the code to generate the `episode_data.csv` file.


Transcripts Data 

This repository contains CSV files with transcripts data extracted from web archives. The data is ready for use and does not require any preprocessing steps. 

Files 

transcripts folder: Include CSV files containing the transcripts data. 

Usage 

1. Download the Data: 
- You can download the CSV file from 
(https://www.kaggle.com/datasets/heheheluke/parks-and-recreation-scripts). 

2. Data Fields: 
- The CSV file includes the following fields :Character and dialogue. 

3. Data Exploration: 
- You can explore the data directly using tools like pandas in Python, Excel, or any other data analysis tool. 



Person Data 

This code processes a CSV file (`merged_output_file.csv`) containing information about people involved in the "Parks and Recreation" show, specifically focusing on names and job titles. 
Code Explanation: 

1. Data Source: The merged CSV file can be created using IMDb and episode data. 

2. Usage: 
- Replace the file path (`csv_file_path`) with the actual path to your merged CSV file. - Run the code to generate the `Person.csv` file.
