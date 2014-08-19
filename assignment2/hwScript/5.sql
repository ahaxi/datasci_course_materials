select count(*) 
from (
	select docid, sum(f.count) c
	from frequency f
	group by docid
	having c > 300
) x;
