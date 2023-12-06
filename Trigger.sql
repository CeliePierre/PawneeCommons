-- database check: making use it's using the right database
use PawneeCommons;

-- if the trigger already exists it drops it
drop trigger if exists check_insert;    
    
DELIMITER //
-- creates trigger
create trigger check_insert
before insert on charactr
for each row
begin
	-- Check the condition for the insert
	if exists (select 1 from charactr as c where c.cFirstName = new.cFirstName and c.cLastName = new.cLastName) then
		-- Rollback the update if the condition is not met
		signal sqlstate '45000'
		set message_text = 'Sorry that name already matchs a characters name in the data base';
	end if;
end //
DELIMITER ;

