-- this script joins two table with a reference to id of the state table



SELECT id, name
FROM cities
WHERE states.name='California'
AND states.id = cities.state_id
ORDER BY id;
