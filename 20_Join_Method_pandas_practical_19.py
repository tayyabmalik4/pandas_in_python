# **********************Join method in pandas****************************

#---------Definition------------- DataFrame hoin is a convenient method for combining the columns of two potentially differently-indexed
# ///////All the dataframes must be same lenght otherwise error accured 

# //////////////discuss about---------(other,on,how,lsuffix,rsuffix)

import pandas as pd
from pandas.core.frame import DataFrame

df1=pd.DataFrame({'A':[1,2,3],'B':[11,12,13]})
df2=pd.DataFrame({'C':[5,6],'D':[15,16]})

print(df1)
print(df2)

# /////starting join function
print(df1.join(df2))
print(df2.join(df1))

# /////if indexes are not same than the dataframes are not join properly
# /////if we want to join the dataframes through join function than the indexes are making the same 


# **********how******
# /////if we want to joins the 2 or more dataframes according to left or right or inner or outer attributes by default left
# /////right means that the DataFrames are join according to 2nd DataFrame
print(df1.join(df2,how='right'))
# /////inner(intersection) means the dataframes printout those values who are same
print(df1.join(df2,how='inner'))
# ////outer(union) means the dataframes prinout those values who are same as well as different 
print(df1.join(df2,how='outer'))


# ////if the dataframe column names are same and we want to join it than we use lsuffix or rsuffix
# ///this function is use to change the column name who are same
df3=pd.DataFrame({'A':[1,2,3],'B':[11,12,13]})
df4=pd.DataFrame({'A':[5,6],'D':[15,16]})
# /////if we want to change the left column name than we use lsuffix
print(df3.join(df4, lsuffix='_1'))
# ////if we want to change the right column name than we use rsuffix
print(df3.join(df4, rsuffix="- 2"))



