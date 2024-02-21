-- Lists all records in second_table with a score >= 10, ordered by score desc
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
