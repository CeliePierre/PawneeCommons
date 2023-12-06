-- database check: making use it's using the right database
use PawneeCommons;

-- sql insert trigger test
-- test - already existing name: 'Leslie' 'Knope'
-- test - new name: 'Samwise' 'Gamgee'
insert into charactr (cID, cFirstName, cLastName)
select COUNT(cID) + 1, 'Leslie', 'Knope'
from charactr;

-- seeing results 
select *
from charactr
