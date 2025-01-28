CREATE TABLE catchersalaries AS
SELECT DISTINCT s.playerID, s.YearID, s.salary, f.POS
FROM Salaries s
JOIN Fielding f ON s.playerID = f.playerID AND s.YearID = f.YearID
WHERE f.POS = 'C'
ORDER BY s.playerID, s.YearID;
