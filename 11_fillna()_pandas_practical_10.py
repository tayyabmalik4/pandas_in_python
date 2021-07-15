# ************************fillna() using pandas in python***************************
# ////////if we want to fill empty values than we use this function----------fillna()

# /////////syntax=DataFrame.fillna()
# ////////discuss about-----(value,method,axis,inplace,limit)


import pandas as pd

fill=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
# print(fill)


# //////if we want to fill the empty values than we use this function-----print(fill.fillna(?))
# ///////value is default
# //////these are same
print(fill.fillna(value="not available"))
print(fill.fillna("not available"))