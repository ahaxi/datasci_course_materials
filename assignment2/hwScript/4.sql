select count(*) from
(
	select distinct docid 
	from frequency
	where term = 'parliament'
) x;
