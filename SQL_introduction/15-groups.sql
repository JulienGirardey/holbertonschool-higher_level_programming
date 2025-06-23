-- that lists the number of records with the
-- same score in the table second_table
select score, count(id) as number
from second_table
group by score;
