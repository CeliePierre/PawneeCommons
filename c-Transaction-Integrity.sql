-- Start the transaction
START TRANSACTION;

-- Update operation within the transaction
UPDATE PawneeCommons.works
SET job = 'cook' -- This value violates the allowed job titles
WHERE pID = 1 AND eID = 's7e12';

-- Set the allowed job titles
SET @allowed_job_titles := 'Cast,written_by,directed_by';

-- Check the integrity constraint
SET @job_check := FIND_IN_SET('cook', @allowed_job_titles COLLATE utf8mb4_general_ci);

-- Variable to store the result of the condition
SET @rollback_required := 0;

-- Check the condition and set the variable accordingly
SELECT IF(@job_check = 0, @rollback_required := 1, @rollback_required);

-- Rollback or commit based on the condition
SELECT CASE
    WHEN @rollback_required = 1 THEN
        -- Rollback the transaction if the constraint is violated
        'Transaction Rolled Back'
    ELSE
        -- Commit the transaction if the constraint is satisfied
        'Transaction Committed'
END AS Result;