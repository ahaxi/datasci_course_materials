select S 
from
(
	SELECT 
		a.docid ldocid
		, b.docid rdocid
		, SUM(a.count * b.count) S
	FROM 
	(	
		frequency a 
		JOIN 
		frequency b 
		ON a.term = b.term
		and a.docid < b.docid 
	)
	GROUP BY a.docid, b.docid 
) x
where x.ldocid = '10080_txt_crude' and x.rdocid = '17035_txt_earn';

