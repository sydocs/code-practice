"""
570. Managers with at Least 5 Direct Reports
https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 

Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+

"""

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Count direct reports per managerId
    counts = (
        employee.dropna(subset=["managerId"])
        .groupby("managerId")
        .size()
        .reset_index(name="cnt")
    )
    
    # Keep only managers with at least 5 reports
    eligible_managers = counts[counts["cnt"] >= 5]
    
    # Join back to get manager names
    result = eligible_managers.merge(
        employee[["id", "name"]],
        left_on="managerId",
        right_on="id",
        how="inner"
    )
    
    return result[["name"]]