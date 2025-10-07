import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
  filtered_students=students['student_id']==101
  result_df=students[filtered_students][["name","age"]]
  return result_df