# Write your MySQL query statement below
SELECT e1.Name as Employee FROM Employee e1
INNER JOIN Employee e2
ON e1.ManagerId = e2.Id
Where e1.Salary > e2.Salary