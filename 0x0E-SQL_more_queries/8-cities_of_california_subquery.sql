-- this script joins two table with a reference to id of the state table



SELECT id, name
FROM cities
WHERE states_id = (SELECT id FROM states WHERE name='California')
ORDER BY id;
