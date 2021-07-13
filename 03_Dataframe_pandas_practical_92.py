# **********************DataFrame in pandas

# /////dataFrame is a two dimentional ,size-mutable(change the size according to over requirment),potentially hetrogenous tabular data structure with labeled axes(rows and colums)

# ////there are many types to creat the dataframe(2d array) 

import pandas as pd
# //////first of all creating empty 2d array using pandas module
df_em=pd.DataFrame([]) 
# print(df_em)


# /////creating the dataFrame(2d array) using list
df_lst=['a','b','c']
# print(df_lst)
# print(pd.DataFrame(df_lst))

# //////if we want to creat the data in list in lists than we use this methid
df_lst1=[[1,2,3],[1,2,3],[1,2,3]]
# print(df_lst1)
# print(pd.DataFrame(df_lst1))


# /////if we want to creat the convert the data in dictionary to 2d array than we use theis method
df_dict={"ID":[11,12,13,13]}
# print(df_dict)
# print(pd.DataFrame(df_dict))


# .//////////if we want to converd the data ----dictionary of dictionary to 2d array than we usse this method
# //////the values are must equal
df_dict1={"ID":[1,2,3,4,5,6],"name":["tayyab","zahid","junaid","uzair","zaheer","mohsan"]}
# print(df_dict1)
# print(pd.DataFrame(df_dict1))

# ////////if we want to creat the data -----list of dictionary to DataFrame(2d array)
df_lst_dict=[{"Name":"Tayyab","Dream":"Sultan's Production"},{"Name":"Junaid","Dream":"Jarviz production"}]
# print(df_lst_dict)
# print(pd.DataFrame(df_lst_dict))


# //////if we want to creat data by the help of series than we use this function
df_ser={"ID":pd.Series([1,2,3,4]),"Name":pd.Series(["Junaid","Zahid","Tayyab","Osama"])}
print(df_ser)
print(pd.DataFrame(df_ser))
 








 
