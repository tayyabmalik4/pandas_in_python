# *****************************concat() tool in pandas library************************
# ---------------concat means to combining connecting the two or more tep DataFrame or Series
# //////parameters------------objs, axis, join, join_axis, ignore_index, keys, sort

import pandas as pd

# /////creating Series
con=pd.Series([0,1,2,3])
con1=pd.Series([4,5,6,7,4])
# print(con)
# print(con1)

# /////starting concat function
# print(pd.concat([con,con1]))

# /////creating DataFrames
con2=pd.DataFrame({"ID":[1,2,3,4,5],
                    "Name":['A','B','C','D','E'],
                    'Class':[4,6,8,10,12]})
con3=pd.DataFrame({"ID":[1,2,3,4,5,6],
                    "Name":['A','B','C','D','E','F'],
                    'Class':[4,6,8,10,12,14]})
# print(con2)
# print(con3)
# //////concat the dataframes using concat function
print(pd.concat([con2,con3]))


# /////if we want to concat the dataFrames as columns wise than we use axis function
# //////rows(0) wise concat is by default
print(pd.concat([con2,con3], axis=1))