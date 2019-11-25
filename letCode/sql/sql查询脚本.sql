INSERT INTO Employee(id, Salary) 
VALUES 
    (5,300) 
SELECT 
	* 
FROM 
	Employee -- 寻找薪水第二高或者第n高的值
SELECT 
	b.SecondHighestSalary 
FROM 
	(
		SELECT 
			a.Salary AS SecondHighestSalary 
		FROM 
			(
				SELECT 
					Salary 
				FROM 
					Employee 
				GROUP BY 
					Salary 
				UNION ALL 
				SELECT 
					NULL AS Salary
			) a 
		ORDER BY 
			a.Salary DESC 
		LIMIT 
			1
	) b 
ORDER BY 
	b.SecondHighestSalary ASC 
LIMIT 
	1 --编写一个 SQL 查询来实现分数排名。如果两个分数相同，则两个分数排名（Rank）相同。请注意，平分后的下一个名次应该是下一个连续的整数值。换句话说，名次之间不应该有“间隔”。
SELECT 
	a.Salary, 
	@rownum := @rownum + 1 AS rank 
FROM 
	Employee a, 
	(
		SELECT 
			@rownum := 0
	) AS b 
ORDER BY 
	a.Salary DESC
	



	
	
	 --	,CASE WHEN a.salary = b.salary THEN @rownum ELSE @rownum := @rownum + 1 END AS rank 
	--优化
SELECT 
	c.salary 
	,CASE WHEN c.salary = c.salary2  THEN @rownum ELSE @rownum := @rownum + 1 END AS rank 
FROM 
	(
		SELECT 
			a.id as id,
			a.salary AS salary, 
			b.id as id2,
			b.salary AS salary2 
		FROM 
			Employee a 
			LEFT JOIN Employee b 
			on a.salary = b.salary 
			and a.id <> b.id
	) c, 
	(
		SELECT 
			@rownum := 1
	) AS d
order by c.salary desc