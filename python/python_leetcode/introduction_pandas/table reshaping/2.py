"""
2889. Reshape Data: Pivot
https://leetcode.com/problems/reshape-data-pivot/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

"""

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(
        index='month',
        columns='city',
        values='temperature'
    )