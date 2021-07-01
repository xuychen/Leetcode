#  Write your MySQL query statement below
SELECT s.Score, DENSE_RANK() OVER(ORDER BY s.Score DESC) as `Rank`
FROM Scores s

# Write your MySQL query statement below
SELECT t.Score Score, cast(t.Rank as signed) `Rank` from Scores s
LEFT JOIN (
    SELECT p.Score Score, @rank:=@rank+1 `Rank`
    FROM (
        SELECT distinct(Score) Score FROM Scores
        ORDER BY Score DESC
    ) p, (SELECT @rank:=0 ) q
) t
on s.Score = t.Score
ORDER BY s.Score DESC