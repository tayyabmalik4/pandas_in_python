# ************************fillna() using pandas in python***************************
# ////////if we want to fill empty values than we use this function----------fillna()

# /////////syntax=DataFrame.fillna()
# ////////discuss about-----(value,method,axis,inplace,limit)


import pandas as pd

fill=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(fill)


# //////if we want to fill the empty values than we use this function-----print(fill.fillna(?))
# ///////value is default
# //////these are same
# print(fill.fillna(value="not available"))
# print(fill.fillna("not available"))


# /////if we want to fill empty values different columns and different values than we  use this function-------print(fill.fillna({'column_name':'fill_value','column_name':'fill_value'}))
# print(fill.fillna({'Date':'None','time':'No Values'}))


# ////if we want to fill the upper values as a default or lower values or pad or None than we use methods(default None)
# /////if we want to fill the upper values in the place of empty values than we use this function-------print(fill.fillna(method='ffill or pad'))
# //////these mathods are same ffill or pad
# print(fill.fillna(method='ffill'))
# print(fill.fillna(method='pad'))


# ////if we want to fill the back values of in the place of empty values than we uses this function----print(fill.fillna(method='bfill or backfill'))
# print(fill.fillna(method='bfill'))
# print(fill.fillna(method='backfill'))


# /////if we want to fill values as colums or as rows than we use axis---column as a default-----
# -----if we want to use this method than we hardly input values or method otherwise it becomes to error
# print(fill.fillna(method='ffill',axis=1))
# print(fill.fillna(method='bfill',axis=1))


# //////if we want to fill the spacific empty values than we use limit function----print(fill.fillna(method or values, limit =int))
# //////limit>0
# ////if we use this function than we must use method or values if we don't use it throgh error
# print(fill.fillna(method='pad',limit=3))


# //////if we want to replace the empty values csv file to non-empty values of csv file than we use inplace function-----print(fill.fillna(method or values, inplace=True)) 
print(fill.fillna(method='ffill',inplace=True))
print(fill)