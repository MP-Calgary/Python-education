I have a SQLite database of baseball statistcs called 'lahmansbaseballdb.sqlite'.

I want to do the following
write a query that gives the result of
salary.playerID, salary.YearId, salary.salary where it joins to the Fielding table, to only get playerID that had a POS = "C"

--
The definition of tables is below:

Table 'Fielding' has columns 'playerID' and 'POS' where pos stands for Position

The unique values of POS are P, OF, 2B, 3B, 1B, SS, C
This is what coresponds to pitcher, catcher, outfielder, but leaving as the code is fine.

-
Table Salaries has columns 'playerID' and their salary in column 'salary'