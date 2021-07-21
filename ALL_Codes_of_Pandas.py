# (1)**************************Pandas****************************
# pip install pandas
import pandas as pd
import os

# (2)***************************Series*******************************************

print(pd.__version__)
lst=[1,2,-3,6.2,'data values']
ser=pd.Series(lst)
ser1=pd.Series([1,2,3,4,5]) 
ser2=pd.Series([ ],dtype=object)
ser3=pd.Series([1,2,3,4,5],index=[1,2,3,4,5])
ser4=pd.Series([12,14,16,18,20],index=[1,2,3,4,5],dtype=float)
ser5 = pd.Series([11,13,15,17,12],dtype=float, name="amazing pandas functionality")
ser6=pd.Series(8)
ser7=pd.Series(8,index=[2,5])
ser8=pd.Series({'a':2,'b':4,'c':45})
ser9=pd.Series([1,2,3,4,5,6,7,8,9])
ser10=pd.Series([11,12,13,14,15,16,17,18,19])
ser11=pd.Series([1,2,3,4,5,6])
print(ser9[3])
print(ser9[2:6]) 
print(ser9.min())
print(ser9[ser9>4])
print(ser9[ser9<5])
print(ser9+ser10)
print(ser9+ser11)


# (3)*************************DataFrame*************************************************

df_em=pd.DataFrame([]) 
df_lst=['a','b','c']
print(pd.DataFrame(df_lst))
df_lst1=[[1,2,3],[1,2,3],[1,2,3]]
print(pd.DataFrame(df_lst1))
df_dict={"ID":[11,12,13,13]}
print(pd.DataFrame(df_dict))
df_dict1={"ID":[1,2,3,4,5,6],"name":["tayyab","zahid","junaid","uzair","zaheer","mohsan"]}
print(pd.DataFrame(df_dict1))
df_lst_dict=[{"Name":"Tayyab","Dream":"Sultan's Production"},{"Name":"Junaid","Dream":"Jarviz production"}]
print(df_lst_dict)
print(pd.DataFrame(df_lst_dict))
df_ser={"ID":pd.Series([1,2,3,4]),"Name":pd.Series(["Junaid","Zahid","Tayyab","Osama"])}
print(df_ser)
print(pd.DataFrame(df_ser))
del df_ser
print(df_ser)
renam=pd.DataFrame({'ID':[1,2,3,4,5],'Name':['A','B','C','D','E']})
print(renam)
print(renam.rename(columns={'ID':'IDs'}))


# (4)***********************************Read CSV and Converting CSV to DataFrame or Series ****************

# //////csv mean --------------coma seperated values
# format ---------------------pd.read_csv(file_link)
csv=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\04_for-converting-csv-to-dataFrame.py-business-financial-data-mar-2021-quarter-csv.csv')
print(csv)
print(os.getcwd())


# (5)********************************Write CSV file**************************************

wr=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(wr)
print(type(wr))
print(wr.columns)
wr1=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',nrows=3)
print(wr1)
wr2=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',usecols=[0])
print(wr2)
wr3=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',usecols=[1,3])
print(wr3)
wr4=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',usecols=[0,2,4])
print(wr4)
wr5=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',skiprows=1)
print(wr5)
wr6=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',skiprows=[13])
print(wr6)
wr7=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',skiprows=[13,14,15,16,17,18])
print(wr7)
print(wr6.count())
wr8=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',index_col='QUESTION NO.')
print(wr8)

# (6)*****************************Write CSV file part 2*************************************

csv1=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(csv1)
csv2=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',header=3)
print(csv2)
csv3=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',header=None)
print(csv3)
csv4=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',header=None,prefix='DATA')
print(csv4)
csv5=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',names=['Code','Question No','Question','A','B','C','D','Ansers'])
print(csv5)

# (7)***************************Write CSV file part 3*******************************************

read=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(read)
print(read.head())
print(read.head(7))
print(read.head(3))
print(read.tail())
print(read.tail(3))                 
read1=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',dtype={'QUESTION NO.':'float32'})
print(read1)            
read2=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',true_values=['yes'])
print(read2)
read3=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',false_values=['No'])
print(read3)

# (8)***********************Handling Missing Values********************************************

# https://pandas.pydata.org/docs/getting_started/index.html
data=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(data)
data1=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',na_values='COMP3112')
print(data1)
data2=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',na_values=['yes','No'])
print(data2)  
data3=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',na_values={'QUESTION NO.':'7','QUESTION NO.':'15'})
print(data3)
data4=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',keep_default_na=False)
print(data4)  
data5=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',na_filter=False)
print(data5)
data6=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv',na_filter=True)
print(data6)


# (9)**********************Handling Missing Values part 2**********************************

var=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(var.isnull())
print(var.isnull().sum())
print(var.isnull().sum().sum())
print(var.notnull())
print(var.notnull().sum())
print(var.notnull().sum().sum())


# (10)********************Handling Missing Values part 3*************************************

csv=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(csv) 
print(csv.dropna())
print(csv.dropna(axis=1))
print(csv.dropna(axis=1,how='any'))
print(csv.dropna(axis=0,how='any'))
print(csv.dropna(axis=1, how='all'))
print(csv.dropna(axis=0,how='all'))
print(csv.dropna(thresh=9))
print(csv.dropna(subset=['Date']))
print(csv.dropna(subset=['time']))
csv1=csv.dropna(inplace=False)
print(csv.dropna(inplace=True))
print(csv)

# (11)*********************Fill the Empty Values using fill function**************************

fill=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(fill)
print(fill.fillna(value="not available"))
print(fill.fillna("not available"))
print(fill.fillna({'Date':'None','time':'No Values'}))
print(fill.fillna(method='ffill'))
print(fill.fillna(method='pad'))
print(fill.fillna(method='bfill'))
print(fill.fillna(method='backfill'))
print(fill.fillna(method='ffill',axis=1))
print(fill.fillna(method='bfill',axis=1))
print(fill.fillna(method='pad',limit=3))
print(fill.fillna(method='ffill',inplace=True))
print(fill)


# (12)*******************Replace the empty values using replace function***********************


rep=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(rep)
print(rep.replace('yes','replace it'))
print(rep.replace(to_replace='yes',value='replace it'))
print(rep.replace([1,2,3,4,5,6],'*'))
print(rep.replace([1,2,3,4,5,6],[11,12,13,14,15,16]))
print(rep.replace({'QUESTION NO.':[1,2,3,4,5,6]},'*'))
print(rep.replace('[A-Za-z]',786,regex=True))
print(rep.replace({'A':'[A-Za-z]','B':'[A-Za-z]','C':'[A-Za-z]','D':'[A-Za-z]'},786,regex=True))
print(rep.replace('yes', method='bfill'))
print(rep.replace('yes',method='bfill',limit=12))
rep.replace('yes','Submitted', inplace=True)
print(rep)


# (13)****************Interpolate(fill the values by guassing the next or previous data)********

inter=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(inter)
print(inter.interpolate())
print(inter.interpolate(method='linear'))
print(inter.interpolate(method='time'))
print(inter.interpolate(method='index'))
print(inter.interpolate(method='nearest'))
print(inter.interpolate(method='polynomial',order=1))
print(inter.interpolate(method='spline',order=1))


# (14)*******************Interpolate part 2******************************************************

inter1=pd.read_csv('F:\\tayyab programming\\machine learning\\pandaswithtayyab\\05_using_write_the_csv_file_merge-sort.csv')
print(inter1)
print(inter1.interpolate())
print(inter1.interpolate(axis=1))
print(inter1.interpolate(limit=2,limit_direction='forward')) 
print(inter1.interpolate(limit_direction='backward')) 
print(inter1.interpolate(limit_direction='both')) 
print(inter1.interpolate(limit_area='inside'))
print(inter1.interpolate(limit_area='outside'))
print(inter1.interpolate(inplace=True))
print(inter1)










