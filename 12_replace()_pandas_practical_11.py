# *******************************   replace() using pandas in python   **********************

# ////if we want to replace the values in excal or any other sheet than we use this function
# Syntax-----var.replace()
# -------------discuss about-------var.replace(to_replace, value, inplace, limit, regex, method)


from os import replace
import pandas as pd

rep=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(rep)

# /////if we want to replace the values in csv sheet than we use replace function
# ////these are same methods 
# print(rep.replace('yes','replace it'))
# print(rep.replace(to_replace='yes',value='replace it'))

  
# /////if we want to change the various values in just one or more values than we use replace function in list-------
# print(rep.replace([1,2,3,4,5,6],'*'))


# /////if we want to various values replace various values than we must the same quantity of values are input there
# print(rep.replace([1,2,3,4,5,6],[11,12,13,14,15,16]))


# /////if we want to replace the some spacific columns values than we use dictionary
# print(rep.replace({'QUESTION NO.':[1,2,3,4,5,6]},'*'))


# //////if we want to convert the string values to integers than we use regex function
# ------------format -----print(rep.replace('[A-Za-z]',int,regex=True))
# print(rep.replace('[A-Za-z]',786,regex=True))

# /////if we want to convert string values to int values or int to str values of spacific column or columns than we use dictionary in regex function
# format-------------------print(rep.replace('to_replace'={'column_name':'[A-Za-z]')},values=int?,regex=True))
# print(rep.replace({'A':'[A-Za-z]','B':'[A-Za-z]','C':'[A-Za-z]','D':'[A-Za-z]'},786,regex=True))


# ////if we want to replace the values upper values or lower(back) values than we use method function
# print(rep.replace('yes', method='bfill'))


# /////if we want to reolace the spacific no of valuezs than we use limit function
# print(rep.replace('yes',method='bfill',limit=12))


# /////if we want to replace the values and modify or update the table than we use the inplace function
rep.replace('yes','Submitted', inplace=True)
print(rep)









