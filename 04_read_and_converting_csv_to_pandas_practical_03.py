# *******************import csv type file in the form of 2d arrays
# //////csv mean --------------coma seperated values
# format ---------------------pd.read_csv(file_link)
# ////////////we import the all types of data e.g Series(1d array), DataFrame(2d array)

# ////////this format is universal form 
# ///////it is easy to use and easy to understand and easy to read and write
# //////this is very easy to Creat and Quick to Creat
# //////it is use in the Data Science and also use in Machine Learning




import pandas as pd
# //////import os module to check that the file where the present
import os


csv=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\04_for-converting-csv-to-dataFrame.py-business-financial-data-mar-2021-quarter-csv.csv')
print(csv)
print(os.getcwd())