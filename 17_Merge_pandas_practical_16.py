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
# print(pd.merge(df1,df2, on='ID'))
# print(pd.merge(df1,df2))
# ////dataFrame merge on right side
# print(pd.merge(df2,df1, on='ID'))

# /////if the ID is not similar than print these values who are same 
# ////if went to show these values than we use how function and the attribute is outer
# print(pd.merge(df1,df2, on='ID', how='inner'))
# print(pd.merge(df1,df2, on='ID', how='left'))
# ///////using right and outer is same functionality
# //////right function is return the float values 
# /////inner means intersection and outer means union
# print(pd.merge(df1,df2, on='ID', how='outer'))
# print(pd.merge(df1,df2, on='ID', how='right'))

# ////if we check that all the values step by step than we use indicator function
# print(df1,df2, on='ID', how='outer',indicator=True)

# //////if all the ID values are differnt than this is 
df3=pd.DataFrame({'ID':[5,6,7,8],'Name':['A','B','C','D']})
print(pd.merge(df1,df3, left_index=True , right_index=True))
df4=pd.DataFrame({'ID':[5,6,7,8],'Name':['A','B','C','D']})

# //////if all dataframes are similar and we input just one columns by the use of on function than by default function is use suffixes to differnce the columns 
# ////and if we want to use different name than we use suffixes function
print(pd.merge(df3,df4,on='ID'))
print(pd.merge(df3,df4,on='ID',suffixes=('_left','_right')))

