# *****************************Pivot Table*************************
# -------definition-------The levels in the pivot table will be stored in multiIndex objects(Hierarchical indexes) on the index and cokumns of the result DataFrame.

# ---------df.pivot_table()
# ---------discuss about(values, index, columns, aggfunc, fill_values, margins, dropna)

from datetime import date, time
import pandas as pd

csv=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(csv)
# //////pivot function is categories the values ----------the same values return one time and the values are mean return

print(csv.pivot_table(index='num'))
print(csv.pivot_table(index='num',columns='ANSWER'))
print(csv.pivot_table(index='num',columns='ANSWER',aggfunc='count'))
print(csv.pivot_table(index='num',columns='ANSWER',aggfunc='sum'))
print(csv.pivot_table(index='num',columns='ANSWER',aggfunc='max'))
print(csv.pivot_table(index='num',columns='ANSWER',aggfunc='min'))
print(csv.pivot_table(index='num',columns='ANSWER',aggfunc='min',fill_value=12))
print(csv.pivot_table(index='num',columns='ANSWER',aggfunc='std'))
print(csv.pivot_table(index='num',columns='ANSWER',aggfunc='min',fill_value=12))
print(csv.pivot_table(index='num',columns='ANSWER',aggfunc='min',fill_value=12,margins=True))


