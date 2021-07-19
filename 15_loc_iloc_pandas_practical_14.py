# **************************loc and iloc function using pandas library in python
# ////syntax---------------print(l.loc[parameters])
# /////definition------------------Acces the group of rows or colums by label(step by step or decorate form) is called loc fucntion 
# /////


from numpy import dtype
import pandas as pd
l=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')

# //////if we want to acces the spacific column than we use this function
# print(l.loc[5])

# ////if we want to acess many rows than we use list in the loc function
# print(l.loc[[1,3,4,5]])


# ////if we want to acces the spacific column and spacific index than we use this function
# print(l.loc[4,"DateTime"])


# //////if we want to acces the some spacific values in one or more columns than we use slicing function
# print(l.loc[1:4,'DateTime'])

# /////if we want to acces these values who greater than spacific values than we use this type of function
# print(l.loc[l['num']>30,['QUESTION NO.']])
# print(dtype(l.num))



# ************************iloc means (int location)***********
# //////it is provides just interger numbers
print(l.iloc[[0]])


# ///////using slicing methods
print(l.iloc[:,3])

# ////using list in iloc
print(l.iloc[[2,3,4]])