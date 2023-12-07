
# README: Trigger-Database Character Management

This Python script provides functionality for managing character information in a MySQL database. It includes features for adding new character names, checking if a name already exists, and retrieving information about a character from the database.

## Prerequisites

Before running the script, ensure you have the following:

1. MySQL server installed and running.
2. Python installed on your machine.
3. Required Python libraries:

```bash
pip install mysql-connector-python
```

## Configuration

The script uses a configuration file ('config.json') to connect to the MySQL database. Make sure to create this file in the same directory as the script with the following structure:

```json
{
  "mysql": {
    "host": "your_host",
    "user": "your_user",
    "password": "your_password",
    "database": "your_database"
  }
}
```

Replace '"your_host"', '"your_user"', '"your_password"', and '"your_database"' with your MySQL server details.

## Usage

1. Run the script:

```bash
python script_name.py
```

Replace 'script_name.py' with the actual name of your Python script.

2. The script will prompt you if you want to add a new character name. Enter "yes" to add a new name or "no" to exit.

3. If adding a new name, provide the character's first and last names.

4. The script will check if the name already exists in the database. If it does, an error message will be displayed, and the changes will be rolled back. If not, the new name will be added.

5. Optionally, you can choose to check where the name is in the database. Enter "yes" to check or "no" to continue without checking.

6. The script will continue prompting you until you enter "no" when asked if you want to add a new name.

## Example

```bash
python character_management.py
```

Follow the on-screen prompts to add or check character names in the database.

## Important Notes

- Ensure that the MySQL server is running and the configuration file ('config.json') is properly set up.
- The script uses a 'charactr' table in the database, so make sure this table exists with the appropriate schema:

```sql
CREATE TABLE charactr (
    cID INT AUTO_INCREMENT PRIMARY KEY,
    cFirstName VARCHAR(255),
    cLastName VARCHAR(255)
);
```

Feel free to customize the script according to your specific database schema and requirements.

---

# README: Transaction Integrity Check

Title: Transaction Integrity Check 

The code performs an update operation on the `PawneeCommons.works` table and checks if the update violates certain constraints. If the constraints are violated, the transaction is rolled back; otherwise, it is committed.

## Code Explanation

1. **Start the Transaction:**
   - The code begins by initiating a transaction. A transaction is a series of one or more SQL statements executed as a single unit.

2. **Update Operation:**
   - An update operation is performed on the `PawneeCommons.works` table. The code attempts to set the job title to 'Producer' for a specific record identified by `pID` and `eID`.

3. **Allowed Job Titles:**
   - A set of allowed job titles (Cast, written_by, directed_by) is specified using the `@allowed_job_titles` variable.

4. **Integrity Constraint Check:**
   - The code checks if the updated job title ('Producer') is in the allowed list using the `FIND_IN_SET` function. The result is stored in the `@job_check` variable.

5. **Condition Evaluation:**
   - A variable, `@rollback_required`, is set to 0 initially. The code then checks if the job title violates the allowed titles and updates the variable accordingly.

6. **Rollback or Commit:**
   - Depending on the condition, the code determines whether to rollback or commit the transaction. If `@rollback_required` is 1, meaning the constraint is violated, the transaction is rolled back; otherwise, it is committed.

7. **Result Output:**
   - The final result is displayed as 'Transaction Rolled Back' or 'Transaction Committed' based on the outcome of the condition.

## Conclusion

This code checks that only specified job titles are allowed in the database, and any update with an invalid title will result in a rollback of the transaction. This is critical for data integrity and consistency of the database.

## Example
You could see examples in "c-transaction-Integrity.pdf".
