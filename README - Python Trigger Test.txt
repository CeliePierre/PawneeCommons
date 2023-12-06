Python Trigger Test


Summary 
        trigger.py is a way to test an insert SQL trigger. It does this by asking the user for a first and last of a character name they want to insert into the database. It uses that name to verify if it’s in the database. If it is it will perform the trigger and rollback. If not it will insert as normal. 


Used 
● Language: python 
● MySQL workbench


Python Installation: 
```bash 
pip install mysql-connector-python


Needed Files 
● all files in SQL folder 
● all files in Data folder
● import_data_to_sql.py
● Trigger.sql
● trigger.py


Setup 
1. Download: Data folder, import_data_to_sql.py, and trigger.py 
2. In MYSQL run all the dbSetup SQL as querys. The dbSetup files should be located in the SQL folder. 
3. Next run import_data_to_sql.py. This will put all the information in the database. You don’t need the rest of the SQL files to run the trigger but if you’d like to run them it won't break the trigger. 
4. Then set up the trigger by running Trigger.sql. 
5. Finally to test the trigger run the Python code trigger.py 


How to Use trigger.py
When you run the code it will give you prompts. The first prompt asks if you'd like to insert a character into the database. If the word “yes” is typed then it will ask for the character's first name. Once that is imputed then it will ask for the character's last name. After that, the trigger will occur. The trigger will check if the character with that first and last name already exists. If the name is a repeat an error message will be displayed and a rollback will take place. If the character's name is unique it will be inserted into the database. After that, it will ask if you'd like to check the location of the character name in the database. If “yes” It will then display the ID and the name. If “no” it will skip this step. It will then ask again if you like to insert another name and the cycle will repeat till the command “exit” is typed.


Troubleshooting: 
        If it shows an error that is the trigger. This trigger occurs if the character with that first and last name typed already exists in the database.