
import os
import mysql.connector
import json

def trigger_test(path_to_data_dir, charFirstName, charLastName):

    with open(path_to_data_dir, "r") as f:
        config = json.load(f)
    connection_config = config["mysql"]
    data_base = mysql.connector.connect(**connection_config)
    # sql command
    select_command= """ 
    INSERT INTO charactr (cID, cFirstName, cLastName)
    SELECT COUNT(cID) + 1, %(fname)s, %(lname)s
    FROM charactr;
    """
   # creating cursor
    cursor_object = data_base.cursor()
    
   # checking if the trigger will occure
   # trigger - if incerting checks if name exists
    try:
     cursor_object.execute(select_command,{'fname': charFirstName, 'lname': charLastName})
     #if excutes will commit changes to database
     data_base.commit()
    except mysql.connector.Error as err:
    # if trigger occures will print error message
     print(f"Error: Sorry that name already matchs a characters name in the data base")
    # rollback the changes
     data_base.rollback()
    finally:
    # closing cursor
     cursor_object.close()
     data_base.close()

    
def checks(path_to_data_dir, charFirstName, charLastName):
    # connecting to database
    with open(path_to_data_dir, "r") as f:
        config = json.load(f)
    connection_config = config["mysql"]
    data_base = mysql.connector.connect(**connection_config)
    # sql command
    second_command="""
    select cID, cFirstName, cLastName
    from charactr as c
    where c.cFirstName = %(fname)s and c.cLastName = %(lname)s
    """
    # cursor
    cursor_object = data_base.cursor()
    cursor_object.execute(second_command,{'fname': charFirstName, 'lname': charLastName})
    myresult = cursor_object.fetchall()
    print(myresult)
    # closing cursor
    cursor_object.close()
    data_base.close()

def main():
    #getting file path
    find_directory = os.path.dirname(os.path.abspath(__file__))
    path_to_data_dir = os.path.join(find_directory, "data/connectorConfig.json")
   
    # adding/checking character names
    contin = True
    while(contin == True):
     stay = input("Would you like to add a name (yes or on): ")
     #exit loop  
     if(stay == "no"):
      contin = False
      print("Done!")
     if (stay == "yes"):
      #first and last name inputs
      # test - already existing name: 'Leslie' 'Knope'
      # test- new name: 'Samwise' 'Gamgee'  
      charFirstName = input("Input character first name: " )
      charLastName = input("Input character last name: " )
    
      #checking if the names already in the database
      trigger_test(path_to_data_dir, charFirstName, charLastName)
      
      # finds the location of the input name
      check = ""
      while(check != "no" and check != "yes"):
       check = input("Would you like to check where the name is in the database (yes or no): ")
       if (check == "yes"):
        checks(path_to_data_dir, charFirstName, charLastName)
       if (check != "no" and check != "yes"):
        print("That input dosn't work type (yes or no) to continue")
     if (stay != "no" and stay != "yes"):
        print("That input dosn't work type (yes or no) to continue")
if __name__ == "__main__":
 main()