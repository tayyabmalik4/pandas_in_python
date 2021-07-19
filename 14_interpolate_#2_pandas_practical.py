# *****************Interpolate function using pandas linbray in python******************

# discuss about-----parameters of interpolate-----------method,axis,limit,inplace,limit_direction,limit_area


import pandas as pd

inter1=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(inter1)
# print(inter1.interpolate())


# /////if we want to fill the missing values using interpolate function in column or row wise than we use axis function
# /////the default axis value is colums(0) and if we want to fill row wise than we use axis=1
# -----NOTE(all rows datatype is same and numaric if it is not same than error throgh)
# print(inter1.interpolate(axis=1))


# /////if we want to fill the values as own requirments and the spacific columns or rows than we use limit function
# print(inter1.interpolate(limit=3))


# //////if we want to fill the values previous or next(forward or backword or both) base than we use limit_direction function
# print(inter1.interpolate(limit=2,limit_direction='forward')) 
# print(inter1.interpolate(limit_direction='backward')) 
# print(inter1.interpolate(limit_direction='both')) 


# ////if we want to fill the empty values in just the program values guess than we use limit_area='inside' function
# print(inter1.interpolate(limit_area='inside'))
# ////and if we want to fill the values out side of the program means other values which we wish than we use limit_area='outside' function
# print(inter1.interpolate(limit_area='outside'))


# /////if we want to replace the empty values csv sheet to fill values sheet using interpolate function than we use inplace=True function
print(inter1.interpolate(inplace=True))
print(inter1)
