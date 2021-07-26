# ********************************Apend function ***************************
# //////pandas append function is used to append rows of other daraframe to the end of the given dataframe, and returning a new dataframe object

# //////////this is the similar to join function
# ////////but it is join the rows and in the joijn function join columns wise


# /////discuss about(other, ignore_index,sort)

import pandas as pd

df1=pd.DataFrame({'A':[1,2,3],'B':[11,12,13]})
df2=pd.DataFrame({'C':[4,5,6],'D':[14,15,16]})

print(df1.append(df2))