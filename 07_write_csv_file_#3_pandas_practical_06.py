# ******************************Write Csv file part 04 by the use of pandas library of python******************
# -------discuss about--------------head(),tail(),dtype, true_values, false_values

# /////importing the pandas library
import pandas as pd


# ///////////importing the csv file
read=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
# print(read)


# //////////////if we want to printout the top upper 5 or spacific(less or more) rows than we use head function in pandas library
# ////////NOTE(top 5 is default and if we want spacific than we write manually)
# print(read.head())
# print(read.head(7))
# print(read.head(3))


# ////////////if we want to printout the bottom top 5 or spacific(less or more) than we use tail() function
# -----------NOTE(bottom top 5 is default---if we set spacific than write manually)
# print(read.tail())
# print(read.tail(3))


# ////////if we want to change the datatype of any spacific colums than we use dtype function
# -----------format----------pd.read_csv(link,dtype={'column_name','datatype})
read1=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',dtype={'QUESTION NO.':'float32'})
# print(read1)


# //////if we want to change values as "yes" to "True" than we use true_values function
# -----------format----------pd.read_csv(link,true_values=['yes'])
read2=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',true_values=['yes'])
print(read2)

# /////if we want to change values as "No" to "false" than we use flase_values function
# -----------format----------pd.read_csv(link,false_values=['No'])
read3=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',false_values=['No'])
print(read3)















