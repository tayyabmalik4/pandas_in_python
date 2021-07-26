# ********************************Apend function ***************************
# //////pandas append function is used to append rows of other daraframe to the end of the given dataframe, and returning a new dataframe object

# //////////this is the same and similar to join function  
# ////////but it is join the rows and in the join function join columns wise
# /////// but Remember that in the append function we join the same column names


# /////discuss about(other, ignore_index,sort)

import pandas as pd

df1=pd.DataFrame({'A':[2,1,3],'B':[12,11,13]})
df2=pd.DataFrame({'A':[4,5,6],'B':[14,15,16]})

# //////starting append function
# print(df1.append(df2))
# print(df2.append(df1))

# /////if we want to ignore the indexes num than we use ignore_index function
print(df1.append(df2,ignore_index=True))


# /////if the column names is different and we want to append it than we use sort function to saving the future error
df3=pd.DataFrame({'A':[1,2,3],'B':[11,12,13]})
df4=pd.DataFrame({'A':[5,6],'D':[15,16]})
print(df3.append(df4, ignore_index=True, sort=False))