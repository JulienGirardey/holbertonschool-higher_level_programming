-- that creates a table second_table in the database
-- hbtn_0c_0 and add multiples rows
create table if not exists second_table (
	id int,
	name varchar(256),
	score int
);
insert into second_table (id, name, score)
values
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
