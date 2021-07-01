# Write your MySQL query statement below
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num

# Write your MySQL query statement below
SELECT DISTINCT Num ConsecutiveNums
FROM(
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY Num ORDER BY Id) rownum,
        ROW_NUMBER() OVER (ORDER BY Id) id2
    FROM LOGS
) t
GROUP BY (id2-rownum), Num
HAVING COUNT(*)>=3
