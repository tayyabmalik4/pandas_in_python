# ****************************concat part 2 in pandas library***********************

import pandas as pd
# //////copied the previous dataFrames concat part 1
con2=pd.DataFrame({'ID':[1,2,3],'Name':['A','B','C'],'Class':[4,6,8]})
# con3=pd.DataFrame({'ID':[1,2,3,4,5,6],'Name':['A','B','C','D','E','F'],'Class':[4,6,8,10,12,14]})
con3=pd.DataFrame({'ID':[6,8,3,4,6],'Name':['U','G','C','D','E'],'Class':[1,9,8,10,23]})
con4=pd.DataFrame({'ID':[8,3,4,6,7],'Name':['G','C','D','E','Y'],'Class':[9,8,10,23,12]})

# ///////in the axis funcction 0 represents the rows and 1 represnts the columns
# print(pd.concat([con2,con3],axis=1))


# //////if we want to output just these values who is similar means who the common than we use the join(inner) function and inner attribute and outer is by default
# //////inner means intersection(common values) and outer means union(all values)
# print(pd.concat([con2,con3],axis=1,join='inner'))
# print(pd.concat([con2,con3],axis=1,join='outer'))

# ////join and join_axis is the same things 
# ////join='inner' and join_axis=[con3.index] are the same things
# ////jooin='outer' and join_axis=[con2.index] are the same behaves
# /////this function is not run in the python 3.9 for some reason 
# print(pd.concat([con2,con3],axis=1, join_axes=[con2.index]))



# ////if we want to wish that the output is tell about the dataFrames than we use key parameter
# print(pd.concat([con2,con3],keys=['First DF','Secend DF']))
# print(pd.concat([con2,con3], axis=1,keys=['First DF','Secend DF']))


# ////if we want to sort the dataframes than we use sort function
# print(pd.concat([con2,con3],sort=True))



# /////////if we wan to new column add and concat it than we use this function
con5=pd.DataFrame({'MARKS':[44,45,46]})
print(pd.concat([con5,con2],sort=False,axis=1))
print(pd.concat([con5,con2]))