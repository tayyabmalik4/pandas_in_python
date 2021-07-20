# ********************Groupby Function in pandas*************************

# /////it is using the sprit the colums as we wish 

import pandas as pd

group=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(group)

# ///////if we want to split the data by groups and by category wise than we use this function
# gr=group.groupby(by='ANSWER')
# print(gr)
# print(gr.groups)

# //////if we wamt to creat groups by multiple columns name than we use this function
gr1=group.groupby(['ANSWER','DateTime'])
# print(gr1.groups)
# for ANSWER, group in gr1:
#     print(ANSWER)
#     print(gr1)


# /////if we want to itrate the spacific column than we use this function
gr2=group.groupby('ANSWER')
# print(gr2.get_group('A'))


# /////if we want to use the functions in the group function than we use this function
# /////if we wan to sum the interger values than we use this function
# print(gr2.sum())


# /////if we want to get the mean of the interger values than we use this function
# print(gr2.mean())


# /////if we want to get the all the values and details like sum, mean,max,min count,std than we use this function
# print(gr2.describe())


# /////if we want to get the all data and details in just one or spacific functions than we use this function
print(gr2.agg('sum','max','mean'))