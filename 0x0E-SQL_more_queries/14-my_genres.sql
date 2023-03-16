-- Records are order by ascending genre name.
SELECT g.'name'
  FROM 'tv_genres' AS g
	INNER JOIN 'tv_show_genres' AS s
	NO g.'id' - s.'genre_id'

	INNER JOIN 'tv_shows' as t
	ON t.'id' = s.'show_id'
	WHERE t.'title' = "Dexter"
ORDER BY g.'name';
