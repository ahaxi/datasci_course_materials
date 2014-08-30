select S from
(
SELECT a.row_num, b.col_num, SUM(a.value * b.value) S
  FROM a JOIN b ON a.col_num = b.row_num
 GROUP BY a.row_num, b.col_num
having a.row_num = 2 and b.col_num = 3) x;
