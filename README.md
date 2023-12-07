# Pawnee Commons Database Documentation

## Project Team
- Célie Pierre
- Sarah Lawrence
- Reihaneh Maarefdoust

## COS 457 Database Systems
December 6, 2023

## Introduction 
Pawnee Commons is a database designed for both creators and fans, providing quick access to information from the TV show Parks and Recreation. The choice of Parks and Recreation was based on the extensive data available, particularly the transcripts. This database enables users to swiftly retrieve details about the cast and crew, characters, episodes, and transcripts.

## Data File 
The Pawnee Commons database was initiated with a combination of pre-existing data and web scraping. The prior information included files such as parks_and_rec_imdb.csv, parks_and_rec_episodes.csv, and transcripts gathered from Kaggle. Reihaneh developed the Python code named "Data Preparation for Database," which organizes the data from these files to adhere to the ER diagram. Web scraping, utilizing organized episode and writer&director CSV files, played a significant role in acquiring cast and character information.

## Part 1 - Entity Relationship Diagram (ERD)
Part one involved creating an entity relationship diagram collaboratively. Célie, Reihaneh, and Sarah divided the workload among themselves, each focusing on specific entities and relationships. The ER diagram mapped out entities such as Person, Works on, Characters, Episodes, Viewers, Plays, Views, and Transcripts. Live feedback was obtained during the presentation.

## Part 2 - Data Gathering, Cleaning, and SQL Commands
In part two, the team worked on gathering and cleaning scraped information, writing SQL commands, and creating a video explaining these commands. Célie, Reihaneh, and Sarah once again distributed the tasks among themselves. Célie wrote SQL commands, converted them into procedures, and created the import_data_to_sql.py script. Reihaneh organized CSV files based on the ER diagram, assisted with SQL commands, and contributed to testing. Sarah handled Python web scraping, organized scraped information, and created the explanation video for this section.

## Part 3 - User Interface, Search Functionalities, and Documentation
Part three involved creating a working user interface and implementing three search functionalities: trigger, join operation, and transaction for the update operation. The team also organized the entire project documentation and code on GitHub. 
