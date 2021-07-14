# **************************************Write csv files using pandas********************************


import pandas as pd
# ///////////import the csv file as following------------
# -----------format---------pd.read_csv(link)
# ////////in this link we write the double slash(\\) to handling errors
csv1=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
# print(csv1)

# //////if we want to choose manually heading than we use this format-----------------pd.read_csv(link,header=?)
# //////but remember that the upper values of the chooosing heading is skiped or not showed
csv2=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',header=3)
# print(csv2)

# /////if there are not header yet than we want to not making the header than we use this format--------------pd.read_csv(link,header=None)
csv3=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',header=None)
# print(csv3)


# //////if there are not heading and we want to write the heading manually in string than we use prefix and names variable
# //////but remember that the header=None is must to be write that if it is not write than we facing the errors
csv4=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',header=None,prefix='DATA')
# print(csv4)


# /////if we want to write and name indiviually every column than we use name function
# ------format-------------pd.read_csv(link,name=?)
csv5=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',names=['Code','Question No','Question','A','B','C','D','Ansers'])
# print(csv5)

