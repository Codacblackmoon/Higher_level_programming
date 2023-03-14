-- links all records of second table where name is not NUL ordered by score
SELECT score, name
FROM second_table
WHERE name IS NOt null
ORDER BY score DESC;
