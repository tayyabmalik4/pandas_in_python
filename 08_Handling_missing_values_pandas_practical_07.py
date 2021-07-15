# ***************************Handling missing values using pandas library in python***********************************************

# ///////if we read the documentry about pandas kibrary than use this link-------https://pandas.pydata.org/docs/getting_started/index.html

# --------discuss about----------(na_values,keep_default_na,nafilter)

# ////////////////////if we want to handle the missing values in any csv file than we use these function/////////////////////////
# //////if some empty boxs yet in the csv file than we want to fill it or check it than we use these functions
# //////if some data is as a raw material means these are boxes is empty buit write something as (nodata,not fill etc) and we want to these boxes are as a empty than we use these functions
# ///////these are the default as a empty boxs----------(#N/A,#N/A N/A,#NA, -1.#IND, -1.#QNAN, -NaN,-nan, NA,NULL,null,n/a,nan, 1.#IND,1.#QNAN)
# //////if these are fill in any box than pandas consider that the box is empty
# //////and if we want to fill manually than we use na_values=?
# /////and if values more than one than we use list na_values=[list]

import pandas as pd


# //////////////for simple to check it
data=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
# print(data)
# ///////for the one convered to null
data1=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',na_values='COMP3112')
# print(data1)

# ////////for multiple boxs to null
data2=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',na_values=['yes','No'])
# print(data2)    


# /////if we want to convered to null just spacific column spacific attribute than we usee dictionary
# ------------format ----------pd.read_csv(link,na_values={'column_name':'attribute_name'})
data3=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',na_values={'QUESTION NO.':'7','QUESTION NO.':'15'})
# print(data3)  


# /////if we want that the default null operations(#N/A,#N/A N/A,#NA, -1.#IND, -1.#QNAN, -NaN,-nan, NA,NULL,null,n/a,nan, 1.#IND,1.#QNAN) are not conseder our program than we use this function----------pd.read_csv(link,keep_default_na)
data4=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',keep_default_na=False)
# print(data4)  



# ////if we want to check that the empty spaces are present or not in the csv file than we use na_filter function in pandas----------pd.read_csv(link,na_filter=True)
# Detect missing value markers (empty strings and the value of na_values). In data without any NAs, passing na_filter=False can improve the performance of reading a large file.
data5=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',na_filter=False)
# print(data5)


# //////if we want to skip the blank spacies or lines than we use this function------(pd.read_csv(link,skip_blank_lines=(default True)))
data6=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',na_filter=True)
print(data6)


















