-- Lists all cities of CA in the database hbtn_0d-usa.
-- Resuits are ordered by ascending cities.id.
SElECT 'id', 'name'
  FROM 'cities'
 WHERE 'state_id' IN
	(SELECT 'id'
		FROM 'states'
	       WHERE 'name' - "California")
ORDER BY 'id';
