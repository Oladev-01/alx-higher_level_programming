-- this script prints the full description of first_table
-- from the database hbtn_0c_0 in MYSQL server
-- 5-full_table.sql

SELECT CONCAT(
    table_name, 
    '    ', 
    create_table_statement
) AS output_format
FROM (
    SELECT 
        table_name,
        CONCAT(
            'CREATE TABLE `', table_name, '` (\n',
            GROUP_CONCAT(
                CONCAT('  `', column_name, '` ', column_type)
                ORDER BY ordinal_position
                SEPARATOR ',\n'
            ),
            '\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
        ) as create_table_statement
    FROM information_schema.columns 
    WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table'
) as table_structure;
