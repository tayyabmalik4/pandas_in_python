# **************************Handling Missing Values part 2 using pandas in python****************

# ///////this is use for DataFrame or Series

# ////////we discuss about ----------------(isnull(), notnull())

# ///////if we want to check that which colums are present null values and we want to show these than we use null function
# ---------------format-----------------(var=pd.read_csv(link)     print(var.isnull()))


import pandas as pd

var=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')


# **********************null values***************************
# ///////the empty values are ture and not empty vlaues are false
# ////check that null values
# print(var.isnull())

# ////if we want to check that all colums step by step and how null values are present than we use this function
# print(var.isnull().sum())


# //////if we want to check the tatoal null values then we use this function
print(var.isnull().sum().sum())




# *8*****************************notnull values **************************
# /////this is the totally opposite of the null function 
# ////if we check that the values of the file how many boxs are not empty or not null than we use this function
# /////the not empty values is true and the empty values are false
print(var.notnull())

# /////if we want to check all the columns step by step how many values are not wmpty then we use this function
print(var.notnull().sum())

# ////if we want to check total non_empty values than we use this function
print(var.notnull().sum().sum())