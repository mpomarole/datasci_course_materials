CREATE VIEW freq AS
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

/* Multiply */
SELECT a.docid, b.term, SUM(a.count*b.count)
  FROM freq as a,
  (SELECT term as docid, docid as term, count from freq) as b
  WHERE a.term = b.docid AND a.docid='q'
  GROUP BY a.docid, b.term;


