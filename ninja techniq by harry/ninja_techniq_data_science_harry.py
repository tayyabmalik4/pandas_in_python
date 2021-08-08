# *******************************for Data analysis using python we take some techniques which we analysis the data with in just 5 mintius*********************************************

# first of all we importinh the csv file which we analyse
# /////this is the housing data in california in america

# importing the libraries
import pandas as pd
import sys
# /////if we generate all the data report in one line code run than we use pandas-profiling library
# ////this is 
from pandas_profiling import profileReport

# /////importing the file using pandas library
df=pd.read_csv('Housing.csv')
# print(df)

# /////Genrate a Report
profile= profileReport(df)
profile.to_file(output_file='housing.html')