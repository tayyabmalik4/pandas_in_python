# ***********************Merge function in pandas**********************
# ////////we connect or merge the colums or rows by using merge function 
# //////this is very helpful for training the machine learning modle

import pandas as pd

df1=pd.DataFrame({'ID':[1,2,3,4],'Class':[3,6,2,5]})
# print(df1)
df2=pd.DataFrame({'ID':[1,2,3,4,5],'Name':['A','B','C','D','E']})
# print(df2)

# ??///////merge function use
# /////data frame merge on left side

# //////if one or more columns are same and we want to wish that these are in one time in dataframe than we use 'on' function in merging tool 
print(pd.merge(df1,df2, on='ID'))
print(pd.merge(df1,df2))
# ////dataFrame merge on right side
print(pd.merge(df2,df1, on='ID'))

# /////if the ID is not similar than print these values who are same 
# ////if went to show these values than we use how function and the attribute is outer
print(pd.merge(df1,df2, on='ID', how='inner'))
print(pd.merge(df1,df2, on='ID', how='outer'))
print(pd.merge(df1,df2, on='ID', how='left'))
print(pd.merge(df1,df2, on='ID', how='right'))

# ////if we
