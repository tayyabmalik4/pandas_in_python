# ////////series in pandas/////////////////
# //////Series is a one dimentional array in pandas
# //////




# ****************import the pandas library
import pandas as pd
# //////checking the version of pandas
# /////the verion is 1.3.0
# print(pd.__version__)

lst=[1,2,-3,6.2,'data values']
# print(lst)


# *******************starting the series function in pandas
# //////to converting the 1d array to table form we use Series function in pandas in python
ser=pd.Series(lst)
# print(ser)
# print(type(ser))
# ///////pandas.core.series.Series=1d array



# //////to creating the Series in short way
ser1=pd.Series([1,2,3,4,5]) 
# print(ser1) 


# //////to creating the empty series in pandas
ser2=pd.Series([ ],dtype=object)
print(ser2)


# /////if we want to write the index manually then we use this function
# /////but the index is equals to the values if it is not equal than it comes to error
ser3=pd.Series([1,2,3,4,5],index=[1,2,3,4,5])
# print(ser3)


# //////if we want to change the data type than we use this function
ser4=pd.Series([12,14,16,18,20],index=[1,2,3,4,5],dtype=float)
# print(ser4)


# /////if we want to insert the name of the object than we use this function
ser5 = pd.Series([11,13,15,17,12],dtype=float, name="amazing pandas functionality")
# print(ser5)


# /////if we want to inserting the single value than we use this function
ser6=pd.Series(8)
# print(ser6)


# /////if we want to creat many index of same nums than we use this function
ser7=pd.Series(8,index=[2,5])
# print(ser7)


# /////////if we want to print the dictionary
# -------in this dictionary key represents the index and values represents the values
ser8=pd.Series({'a':2,'b':4,'c':45})
# print(ser8)


ser9=pd.Series([1,2,3,4,5,6,7,8,9])
ser10=pd.Series([11,12,13,14,15,16,17,18,19])
ser11=pd.Series([1,2,3,4,5,6])
# print(ser9)
# ///////if we want to acces the array in spacific element than we use this function
# print(ser9[3])

# //////if we want acces two or more elements of the array than we use slicing function
# print(ser9[2:6]) 

# /////if we want to acces the maximum value than we use this function
# print(ser9.max())

# /////if we want to acces the minmum value than we use min f=unction
# print(ser9.min())


# /////if we want to printout that the numbers greater or lesser than we use operaters in pandas
# print(ser9[ser9>4])
# print(ser9[ser9<5])


# ////if we want to add the 2 same arrays then we use add operator or + operator 
# /////if the number of indexs are not same its also work well and it is the functionality of pandas
print(ser9+ser10)
# /////handling emplty datas
# /////NaN means the Not a Number
print(ser9+ser11)




