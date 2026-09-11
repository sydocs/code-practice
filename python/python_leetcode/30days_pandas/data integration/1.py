"""
1050. Actors and Directors Who Cooperated At Least Three Times
https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

Table: ActorDirector

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
timestamp is the primary key (column with unique values) for this table.
 

Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
ActorDirector table:
+-------------+-------------+-------------+
| actor_id    | director_id | timestamp   |
+-------------+-------------+-------------+
| 1           | 1           | 0           |
| 1           | 1           | 1           |
| 1           | 1           | 2           |
| 1           | 2           | 3           |
| 1           | 2           | 4           |
| 2           | 1           | 5           |
| 2           | 1           | 6           |
+-------------+-------------+-------------+
Output: 
+-------------+-------------+
| actor_id    | director_id |
+-------------+-------------+
| 1           | 1           |
+-------------+-------------+
Explanation: The only pair is (1, 1) where they cooperated exactly 3 times.

"""

import pandas as pd

def actors_and_directors(ActorDirector: pd.DataFrame) -> pd.DataFrame:
    result = (
        ActorDirector
        .groupby(['actor_id', 'director_id'])
        .size()
        .reset_index(name='cnt')
    )

    result = result[result['cnt'] >= 3][['actor_id', 'director_id']]
    
    return result