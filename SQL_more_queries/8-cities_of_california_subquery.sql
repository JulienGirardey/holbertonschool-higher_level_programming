-- that lists all the cities of California
-- that can be found in the database hbtn_0d_usa
SELECT cities.id, cities.name
FROM states, cities
WHERE cities.id = states.state_id AND states.name = 'California'
ORDER BY cities.id;
