select count(*) 
from (
	select docid
	from frequency
	where term = 'transaction'
	intersect
	select docid
	from frequency
	where term = 'world'
) x;
