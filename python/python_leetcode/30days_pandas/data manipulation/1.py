"""
177. Nth Highest Salary
https://leetcode.com/problems/nth-highest-salary/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

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
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+

"""

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = (
        employee['salary']
        .drop_duplicates()
        .sort_values(ascending=False)
        .reset_index(drop=True)
    )

    result = salaries.iloc[N - 1] if 1 <= N <= len(salaries) else None

    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})