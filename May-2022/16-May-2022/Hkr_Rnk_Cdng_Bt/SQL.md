Note : Show Command will not wrk in SQl server Because it is My_SQL only CCommand
1. To list all Databases in SQL Server,
Select * from sys.databases 


2. To exclude in-built DBs,
Select * from sys.databases WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb');

3. 