"""
176. Second Highest Salary
https://leetcode.com/problems/second-highest-salary/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+

"""

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # get distinct salaries
    salaries = employee["salary"].dropna().unique()
    
    # sort descending
    salaries = sorted(salaries, reverse=True)
    
    # pick second highest if it exists
    if len(salaries) < 2:
        result = None
    else:
        result = salaries[1]
    
    return pd.DataFrame({"SecondHighestSalary": [result]})