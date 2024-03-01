-- this script displays the cities in the database



SELECT  DISTINCT cities.id, cities.name, states.name
FROM cities, states
ORDER BY cities.id;
