-- Records are order by ascending genre name.
SELECT t.'title' g.'name'
  FROM 'tv_shows' AS t
	LEFT JOIN 'tv_show_genres' AS s
	ON t.'id' - s.'show_id'

	LEFT JOIN 'tv_genres' as g
	ON s.'id' = g.'genre_id'
	WHERE g.'name' = "Comedy"
ORDER BY t.'title', g.'name';
