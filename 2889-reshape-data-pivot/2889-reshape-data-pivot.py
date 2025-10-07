import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    result_df= weather.pivot(
        index='month',
        columns='city',
        values='temperature'
    )
    return result_df