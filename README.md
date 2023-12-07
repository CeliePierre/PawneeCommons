# README: Import Data to SQL

## Overview

This Python script, 'import_data_to_sql.py', is part of the COS 457 Database Systems Project Part 2. Its primary purpose is to import data from CSV files into a MySQL database. The script handles multiple tables, including 'charactr', 'person', 'episode', 'transcripts', 'viewers', 'plays', 'works', 'views', 'scripts', and 'says'.

## Project Information

- **Author:** Célie Pierre
- **Course:** COS 457 Database Systems
- **Project Part:** 2
- **Due Date:** November 20, 2023

## Script Structure

The script is organized into several functions, each responsible for reading and importing data for a specific table. The tables include 'charactr', 'person', 'episode', 'transcripts', 'viewers', 'plays', 'works', 'views', 'scripts', and 'says'. Each table has a corresponding CSV file with the necessary data.

## Functions

### 'read_[name]' Functions

- These functions read data from the respective CSV files and store it in dictionaries.
- The data is then returned in a dictionary format.

### 'insert_table' Function

- This function takes the directory, SQL configuration file, and information for each table.
- It utilizes the read functions to fetch data from CSV files.
- The data is then inserted into the corresponding MySQL tables.

## Table Information

- **'charactr':** Character information, including 'cID', 'cFirstName', and 'cLastName'.
- **'person':** Person information, including 'pID', 'pFirstName', and 'pLastName'.
- **'episode':** Episode information, including 'eID', 'season', 'episode', 'title', 'airDate', and 'descript'.
- **'transcripts':** Transcript information, including 'lID', 'lineNum', and 'dialogue'.
- **'viewers':** Viewer information, including 'vID', 'rating', 'votes', and 'viewers'.
- **'plays':** Plays information, linking characters and persons.
- **'works':** Works information, linking persons and episodes.
- **'views':** Views information, linking viewers and episodes.
- **'scripts':** Script information, linking episodes and lines.
- **'says':** Says information, linking characters, persons, episodes, and lines.

## Usage

1. Open the script 'import_data_to_sql.py' in a text editor.

2. Ensure that the necessary MySQL connector is installed. If not, install it using:

    ```bash
    pip install mysql-connector-python
    ```

3. Update the file paths and information for each table according to your system paths and data.

4. Run the script:

    ```bash
    python import_data_to_sql.py
    ```

5. The script will connect to the MySQL database and import the data into the respective tables.

## Notes

- The script uses the 'mysql.connector' library for database connections.

- Make sure to customize the file paths and table information based on your system and project structure.

- Ensure that the MySQL server is running and accessible.

- Review the SQL schema and CSV file formats to ensure compatibility.
```
