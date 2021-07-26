# ****************************melt funtion ********************************
# -----definition-------pandas melt function is used to transform or reshape the data

# -----syntex-----------------pandas.melt()
# -----discuss about(frame, id_var,value_vars, var_name, value_name)

import pandas as pd

melt=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(melt)

print(pd.melt(melt))
print(pd.melt(melt,id_vars=['QUESTION NO.','Date']))
print(pd.melt(melt,id_vars=['QUESTION NO.'],value_vars=['Date']))
# ///////////to change the variable name we use var_name
print(pd.melt(melt,id_vars=['QUESTION NO.'],value_vars=['Date'],var_name='datee'))
# //////////to change the value name we use value_name function
print(pd.melt(melt,id_vars=['QUESTION NO.'],value_vars=['Date'],var_name='datee',value_name='All Data'))