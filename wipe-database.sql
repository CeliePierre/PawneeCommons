/*
The file import_data_to_sql.py will only run once.
If you need to rerun the file, you need to wipe the database.
You can use the code below to wipe the database.
Once the database has been wiped, rerun import_data_to_sql.py to re-import the data.
*/

-- CAUTION: This will delete all the data in the database.

delete from says;
delete from scripts;
delete from works;
delete from plays;
delete from views;
commit;
delete from charactr;
delete from episode;
delete from person;
delete from viewers;
delete from transcripts;

-- To test if delete was successful
-- Should return NULL for all
select *
from transcripts
