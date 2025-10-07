import pandas as pd
def createDataframe(student_data):
    
    
    student_df=pd.DataFrame(student_data,columns=       ['student_id','age'])
    
    return student_df     