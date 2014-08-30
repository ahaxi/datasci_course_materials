SELECT 
	SUM(a.count * b.count) S
FROM 
(	
	frequency a 
	JOIN 
	frequency b 
	ON a.term = b.term
	and a.docid = '10080_txt_crude'
	and b.docid = '17035_txt_earn'
);

