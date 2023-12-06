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