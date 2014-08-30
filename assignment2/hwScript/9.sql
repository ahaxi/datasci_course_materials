SELECT 
	max(x.S)
FROM
(
	SELECT 
		a.docid, b.docid, SUM(a.count * b.count) S
	from (
		SELECT 'q' as docid, 'washington' as term, 1 as count 
		UNION
		SELECT 'q' as docid, 'taxes' as term, 1 as count
		UNION 
		SELECT 'q' as docid, 'treasury' as term, 1 as count
	) a
	JOIN
	frequency b
	ON a.term = b.term
	Group by a.docid, b.docid
) x;
