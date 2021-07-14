# **************************Write the csv file by using the pandas library in python


# ///////


import pandas as pd
wr=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
# wr=pd.read_csv('F:\\tayyab programming\machine learning\pandaswithtayyab\\04_for-converting-csv-to-dataFrame.py-business-financial-data-mar-2021-quarter-csv.csv')
# print(wr)

# /////if we want to check the data types than we use this function 
# ------------'pandas.core.frame.DataFrame' ------this means that the type is DataFrame and this is the pandas module
# print(type(wr))


# //////if we want to check the colume name then we use this functin
# print(wr.columns)

# ////if we want to read the some spacific rows then we use this function
# ?///////format------------------pd.read.csv(link,nrows=?)
wr1=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',nrows=3)
# print(wr1)


# ////if we want to read the some spacific colums then we use this function
# ----------------format-----------------pd.read.csv(link,usecols=[list_of_index])
wr2=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',usecols=[0])
# print(wr2)
wr3=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',usecols=[1,3])
# print(wr3)
# /////for multiply colums printed
wr4=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',usecols=[0,2,4])
# print(wr4)

# //////if we want to skip any row then we use skiprows function
# /////if we use this function than the rows is skiped and replaced the other data
wr5=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',skiprows=1)
# print(wr5)
# /////if we want to skip the spacific rows than we use list
wr6=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',skiprows=[13])
# print(wr6)
# /////for multi rows skipped function
wr7=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',skiprows=[13,14,15,16,17,18])
# print(wr7)
# print(wr6.count())


# /////if we want top change the columns heading than we use the index_col function
# -------FORMAT-----------------pd.read_csv(link,index_col="colume_name")
# -------FORMAT-----------------pd.read_csv(link,index_col=index_no)

wr8=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',index_col='QUESTION NO.')
# print(wr8)




 

