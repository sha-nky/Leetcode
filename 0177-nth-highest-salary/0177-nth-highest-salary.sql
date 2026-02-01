CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N-1;
  RETURN (
    Select distinct salary
    from employee
    order by salary desc
    limit M, 1
  );
END