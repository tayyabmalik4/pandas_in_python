# ****************************concat part 2 in pandas library***********************

import pandas as pd
# //////copied the previous dataFrames concat part 1
con2=pd.DataFrame({"ID":[1,2,3,4],
                    "Name":['A','B','C','D'],
                    'Class':[4,6,8,10]})
con3=pd.DataFrame({"ID":[1,2,3,4,5,6],
                    "Name":['A','B','C','D','E','F'],
                    'Class':[4,6,8,10,12,14]})

# ///////in the axis funcction 0 represents the rows and 1 represnts the columns
# print(pd.concat([con2,con3],axis=1))


# //////if we want to output just these values who is similar means who the common than we use the join(inner) function and inner attribute and outer is by default
# //////inner means intersection(common values) and outer means union(all values)
print(pd.concat([con2,con3],axis=1,join='inner'))
print(pd.concat([con2,con3],axis=1,join='outer'))

# ////join and join_axis is the same things \
# ////join='inner' and join_axis=[con3.index] are the same things
# ////jooin='outer' and join_axis=[con2.index] are the same behaves
print(pd.concat([con2,con3],axis=1, join_axes=[con3.index]))