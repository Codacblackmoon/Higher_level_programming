-- List all cities in the database hbtn_0d_usa.
-- REcords are sorted in order of ascending cities.id.
SELECT c.'id', c.'name', s.'name'
  FROM 'cities' As c
	INNER JOIN 'states' AS s
	ON c.'state_id' = s.'id'
ORDER BY c.'id';
