INSERT INTO Employee(id, Salary) 
VALUES 
    (5,300) 
    
    
SELECT 
	* 
FROM 
	Employee 
	
	
-- 寻找薪水第二高或者第n高的值
select
	b.SecondHighestSalary
from	
(select
	a.Salary as SecondHighestSalary
from 
(SELECT  
	Salary 
FROM 
	Employee 
group by Salary
UNION ALL 
SELECT 
	NULL AS Salary) a 
order by a.Salary desc 
limit 1) b 
order by b.SecondHighestSalary asc
limit 1


--编写一个 SQL 查询来实现分数排名。如果两个分数相同，则两个分数排名（Rank）相同。请注意，平分后的下一个名次应该是下一个连续的整数值。换句话说，名次之间不应该有“间隔”。
