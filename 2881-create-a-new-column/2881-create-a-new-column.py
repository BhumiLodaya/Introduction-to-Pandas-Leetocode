import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    new_coloumn= employees['bonus']= employees['salary']*2
    return employees