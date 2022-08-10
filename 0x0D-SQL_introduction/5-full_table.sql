-- a script that prints the full description of the table

SELECT *

FROM INFORMATION_SCHEMA.COLUMNS

WHERE table_name = 'first_table'
