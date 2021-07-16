# *********************************Interpolate function using pandas using pythom***********************
# //////////Interpolate is very powerful function.
#  Basically Interpolate is use to fill the data by guassing the previous or next data
# -------------discuss about-----------------(method,axis,limit,inplace,limit_direction,limit_area)
# //////NOTE(It is use just the numarical values)

# /////this is very usefull function in pandas

import pandas as pd

inter=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(inter)

# //////////it is default method=linear
# ///////these are same functions
# print(inter.interpolate())
# print(inter.interpolate(method='linear'))

# //////if we want to fill values as we wish than we use these functions

#  //////if we want to fill the values by the passage of time than we use method='time' function
# /////it is possible just when the indexing value is datetime otherwise the proggram is getting throgh error------(time-weighted interpolation only works on Series or DataFrames with a DatetimeIndex)
# print(inter.interpolate(method='time'))


# /////if we want to fill the values as a index than we use method='index' function in 
# print(inter.interpolate(method='index'))

# ////if we want to fill the values as a nearest values than we use mathod='nearest' function
# /////this is return the value if Scipy is installed using pip otherwise errors accures
# print(inter.interpolate(method='nearest'))

# //////if we want to filling the values as the previous of polynomiual than we use -----------method='polynomial',order=?------ function
# /////if we want to use this function then order is must be input
# print(inter.interpolate(method='polynomial',order=1))

# ////if we want to fill the values as the rectangular form than we use -------------method='spline', order=? function
print(inter.interpolate(method='spline',order=1))



