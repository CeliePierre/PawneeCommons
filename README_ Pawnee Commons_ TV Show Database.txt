README: Pawnee Commons: TV Show Database


 Introduction
Welcome to Pawnee Commons, a TV show database for fans and creators. This Python application uses PySimpleGUI for the graphical user interface and connects to a MySQL database to provide information about episodes, transcripts, characters, and more.


 Getting Started
Before running the code, make sure to set up a MySQL database and update the `config.json` file with your database connection details.


```json
{
  "mysql": {
    "host": "your_host",
    "user": "your_username",
    "password": "your_password",
    "database": "your_database"
  }
}
```


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
- Make sure to have the required Python packages installed (`mysql.connector`, `PySimpleGUI`).


 Authors
- Célie Pierre
- Sarah Lawrence
- Reihaneh Maarefdoust


 Acknowledgments
This project was developed as part of the COS 457 Database Systems course at the University of Southern Maine in the fall of 2023.


Feel free to reach out for any questions or feedback!