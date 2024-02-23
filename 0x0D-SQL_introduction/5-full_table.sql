-- this script prints the full description of first_table
-- from the database hbtn_0c_0 in MYSQL server
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'first_table';
