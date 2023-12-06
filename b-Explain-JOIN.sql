EXPLAIN format=tree SELECT
    pl.pID,
    pl.pFirstName,
    pl.pLastName,
    GROUP_CONCAT(DISTINCT w.job ORDER BY w.job ASC) AS job_titles,
    GROUP_CONCAT(DISTINCT e.season ORDER BY e.season ASC) AS season_numbers
FROM PawneeCommons.plays p
JOIN PawneeCommons.person pl ON p.pID = pl.pID
JOIN PawneeCommons.works w ON p.pID = w.pID
LEFT JOIN PawneeCommons.episode e ON w.eID = e.eID
GROUP BY pl.pID, pl.pFirstName, pl.pLastName
HAVING COUNT(DISTINCT w.job) > 1;

SHOW WARNINGS