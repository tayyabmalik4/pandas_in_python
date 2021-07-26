# ********************************Datetimeindex function*****************************
# -----------definition-----------if we want to chnage the data colum to datetime column than we use this function

import pandas as pd

dat=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(dat)
print(dat.dtypes)
print(type(dat.DateTime[0]))

# ////////starting to change the datatype
dat1=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',parse_dates=['DateTime'])
print(dat1.dtypes)
print(type(dat1.DateTime[0]))