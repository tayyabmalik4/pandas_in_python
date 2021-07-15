# ******************************Handling Missing values part 3 using pandas in python*****************************

# /////discuss about (dropna())
# /////dropna() function basically which colums or rows are exists the empty values and we want to drop this colums or rows  than we use dropna() function


# /////it drop bydefault rows -----print(csv.dropna())------and if we want to drop the colums than we use this function-------print(csv.dropna(axis=1))


# ////if we want to drop these rows(default) or colums who are present the null values than we use ------print(csv.dropna(axis=? ,how='any' ))-----any is a default
# if we want to drop those colums or rows who are all null values than we use this function---------print(csv.dropna(axis=?, how='all'))

# /////////if we want to drop these colums who are miminum 1 or more values are non-empty than we use this function-------print(csv.dropna(thresh=?))


# /////if we want drop the spacific row or column than we use this function----------print(csv.dropna(subset=['column_name']))

# /////if we want to replace the csv sheet which are not present in empty values than we use this function-------print(csv.dropna(inplace=True)) 




import pandas as pd

csv=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
# print(csv) 

# /////it drop bydefault rows -----print(csv.dropna())
# print(csv.dropna())


# //////and if we want to drop the colums than we use this function-------print(csv.dropna(axis=1))
# print(csv.dropna(axis=1))


# /////////if we want to drop these rows(default) or colums who are present the null values than we use ------print(csv.dropna(axis=? ,how='any' ))-----any is a default
# /////for colums
# print(csv.dropna(axis=1,how='any'))

# /////for rows
# print(csv.dropna(axis=0,how='any'))


# if we want to drop those colums or rows who are all null values than we use this function---------print(csv.dropna(axis=?, how='all'))
# //////for colums
# print(csv.dropna(axis=1, how='all'))
# /////for rows
# print(csv.dropna(axis=0,how='all'))



# //////if we want to drop down these boxs who are minimum one or more values are not-empty than we use this function-------print(csv.dropna(thresh=?))
# print(csv.dropna(thresh=9))

# ////////if we want to drop the spacific rows or colums which the empty values are present than we use this function--------print(csv.dropna(subset=['column_name']))
# print(csv.dropna(subset=['Date']))
# print(csv.dropna(subset=['time']))


# /////if we want to replace the csv sheet which are not present in empty values than we use this function-------print(csv.dropna(inplace=)) 
# csv1=csv.dropna(inplace=False)
print(csv.dropna(inplace=False))
