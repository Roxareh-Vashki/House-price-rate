#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


#data = open(r"C:\Users\rokhs\OneDrive\Documents\projects\house\2021\CI\98-401-X2021006CI_English_CSV_data_Ontario.csv")
#data = csv.reader(data)
#print(data)


# In[ ]:


# file = r'C:\Users\rokhs\OneDrive\Documents\projects\house\2021\C\98-401-X2021006_English_CSV_data_Ontario.csv'
# c = 0
# with open(file, 'r') as f:
#     for line in f:
#         print(line)
#         c+=1
#         if c == 300: 
#             break


# In[ ]:


df = pd.read_csv(r'C:\Users\rokhs\OneDrive\Documents\projects\house\2021\C\98-401-X2021006_English_CSV_data_Ontario.csv', encoding = "latin-1", nrows=3000000)


# In[ ]:


df['CHARACTERISTIC_NAME'].unique()
#df_data = df[["CHARACTERISTIC_NAME", "C1_COUNT_TOTAL"]]
#df.iloc[9:12, 200:500]


# In[ ]:


#for col in df.columns:
#    print(col)


# In[ ]:


#file = pd.read_csv(
#    r'C:\Users\rokhs\OneDrive\Documents\projects\house\2021\C\98-401-X2021006_English_CSV_data_Ontario.csv', 
#    encoding="latin-1", 
#    skiprows=6737617,
#    nrows=1977,
#    header=None
#)


# In[ ]:


#df.iloc[:, 0:46]


# In[ ]:


file_name = r'C:\Users\rokhs\OneDrive\Documents\projects\house\2021\C\98-401-X2021006_English_CSV_data_Ontario.csv'

# The starting line for the cities you're interested in
code_list = [6737617,10209230
, 20147609,9034892, 9705095,8463539
, 8461562

]

# Create empty dataframe
df = pd.DataFrame()

# Loop through the code in code_list and concat it with the empty dataframe
for code in code_list:
    tmp = pd.read_csv(
        file_name, 
        encoding="latin-1", 
        skiprows=code,
        nrows=1977,
        header=None
    )
    df = pd.concat([df, tmp])

# Get column headers
header = pd.read_csv(file_name,encoding="latin-1", nrows=0)

# rename Columns
df.columns=header.columns


# In[ ]:


df.head()


# In[ ]:


df.columns


# In[ ]:


data=df[['CENSUS_YEAR', 'ALT_GEO_CODE', 'GEO_NAME', 'CHARACTERISTIC_NAME', 'C1_COUNT_TOTAL']]
data


# In[ ]:


data.count()


# In[ ]:


#data.value_counts()


# In[ ]:


#checking if all Ajax have the same ALT_GEO_CODE
A=df[df['GEO_NAME']=='Ajax, Town (T)']
A[['ALT_GEO_CODE']].count()


# In[ ]:


# for index, row in df.iterrows():
#    print(row['GEO_NAME'], row['CHARACTERISTIC_NAME'], row['C1_COUNT_TOTAL'])


# In[ ]:


# data_dict = dict()
# for index, row in df.iterrows():
#     data_dict.update({data.loc[row, 'GEO_NAME'], data.loc[row, 'CHARACTERISTIC_NAME']}) 


# In[ ]:


# data_dict = dict()
# for values in df[['GEO_NAME','CHARACTERISTIC_NAME']]:
#     data_dict.update({values})


# In[ ]:


data_dict = {"Ajax" : 6737617 , "Aurora" : 10209230 , "Brampton": 20147609
, "Markham" : 9034892 , "Richmondhill" : 9705095 , "Voughan" : 8463539, "York" : 8461562}

for x , y in data_dict.items():
    region = x
    row = y
    print (x , y)
    


# In[ ]:


data.iloc[110:286]


# In[ ]:


# from pandas.core.reshape.concat import concat
# x = data['CHARACTERISTIC_NAME']
# y = data['C1_COUNT_TOTAL']
# list_agg = data.groupby(by='GEO_NAME').agg({lambda x: list(x), lambda y: list(y)})
# list_agg


# In[ ]:


# dictionary = dict(zip(x, y))
# dictionary


# In[ ]:


# from pandas.core.reshape.concat import concat
# list_agg = data.groupby(by='GEO_NAME').agg({lambda x: list(x)})
# list_agg


# In[ ]:


from pandas.core.reshape.concat import concat
grouped = data.groupby(by='GEO_NAME')
#list_agg = grouped.agg([('CHARACTHERISTIC_NAME':lambda x: list(x), 'C1_COUNT_TOTAL':lambda x: list(x) )])


# In[ ]:


# cities_list = ['Ajax, Town (T)', 'Aurora, Town (T)', 'Brampton, City (CY)', 'Markham, City (CY)', 'Richmond Hill', 'Vaughan, City (CY)', 'York, Regional municipality (RM)']
# def df_cities(data,):
#     for x in cities_list:
#         A=data[data['GEO_NAME']=='Ajax, Town (T)']
        
#     return 


# In[ ]:


def sum_group_characteristics(data, match_str):
    return data[data['CHARACTERISTIC_NAME'].str.contains(match_str)].loc[: , ['GEO_NAME' , 'C1_COUNT_TOTAL']]

print(sum_group_characteristics(data, 'Median total income in 2020 among recipien'))


# In[ ]:


income_df = data[data['CHARACTERISTIC_NAME'].str.contains('Median total income in 2020 among recipien')].loc[: , ['GEO_NAME' , 'C1_COUNT_TOTAL']]
print(income_df)


# In[ ]:


income = income_df.rename(columns = {'C1_COUNT_TOTAL' : 'Median total income in 2020 among recipient'})


# In[ ]:


familysize_df = data[data['CHARACTERISTIC_NAME'].str.contains('Average size of census families')].loc[: , ['GEO_NAME' , 'C1_COUNT_TOTAL']]
familysize = familysize_df.rename(columns = {'C1_COUNT_TOTAL' : 'Average size of census families 2020'})
familysize


# In[ ]:


income_family = income.merge(familysize , how= 'right')
income_family


# In[ ]:


a = data[data['GEO_NAME']=='Ajax, Town (T)']
au = data[data['GEO_NAME']=='Aurora, Town (T)']
br = data[data['GEO_NAME']=='Brampton, City (CY)']
ma = data[data['GEO_NAME']=='Markham, City (CY)'] 
ri = data[data['GEO_NAME']=='Richmond Hill, Town (T)'] 
va = data[data['GEO_NAME']=='Vaughan, City (CY)'] 
yo = data[data['GEO_NAME']=='York, Regional municipality (RM)'] 


# In[ ]:


Ajax_languages = a.iloc[[381, 382, 669, 965, 628]][['CENSUS_YEAR', 'ALT_GEO_CODE', 'GEO_NAME', 'CHARACTERISTIC_NAME', 'C1_COUNT_TOTAL']]
Aurora_languages = au.iloc[[380, 381, 668, 964, 627]][['CENSUS_YEAR', 'ALT_GEO_CODE', 'GEO_NAME', 'CHARACTERISTIC_NAME', 'C1_COUNT_TOTAL']]
Brampton_languages = br.iloc[[380, 381, 668, 964, 627]][['CENSUS_YEAR', 'ALT_GEO_CODE', 'GEO_NAME', 'CHARACTERISTIC_NAME', 'C1_COUNT_TOTAL']]
Markham_languages = ma.iloc[[380, 381, 668, 964, 627]][['CENSUS_YEAR', 'ALT_GEO_CODE', 'GEO_NAME', 'CHARACTERISTIC_NAME', 'C1_COUNT_TOTAL']]
RichmondHill_languages = ri.iloc[[380, 381, 668, 964, 627]][['CENSUS_YEAR', 'ALT_GEO_CODE', 'GEO_NAME', 'CHARACTERISTIC_NAME', 'C1_COUNT_TOTAL']]
Vaughan_languages = va.iloc[[380, 381, 668, 964, 627]][['CENSUS_YEAR', 'ALT_GEO_CODE', 'GEO_NAME', 'CHARACTERISTIC_NAME', 'C1_COUNT_TOTAL']]
York_languages = yo.iloc[[380, 381, 668, 964, 627]][['CENSUS_YEAR', 'ALT_GEO_CODE', 'GEO_NAME', 'CHARACTERISTIC_NAME', 'C1_COUNT_TOTAL']]
frames = [Ajax_languages, Aurora_languages,Brampton_languages,Markham_languages,RichmondHill_languages,Vaughan_languages,York_languages]

result = pd.concat(frames)
result


# In[ ]:


result.groupby('CHARACTERISTIC_NAME')['C1_COUNT_TOTAL'].sum()


# In[ ]:


import pyodbc

# insert data from csv file into dataframe.
# working directory for csv file: type "pwd" in Azure Data Studio or Linux
# working directory in Windows c:\users\username
#df = pd.read_csv("c:\\user\\username\department.csv")
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'ROX' 
database = 'AdventureWorks' 
username = 'ROX\rokhs' 
password = 'yourpassword' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
# Insert Dataframe into SQL Server:
for index, row in df.iterrows():
     cursor.execute("INSERT INTO HumanResources.DepartmentTest (DepartmentID,Name,GroupName) values(?,?,?)", row.DepartmentID, row.Name, row.GroupName)
cnxn.commit()
cursor.close()


# In[ ]:


data.iloc[378:704][["GEO_NAME", "CHARACTERISTIC_NAME", "C1_COUNT_TOTAL"]]


# In[ ]:


new_df = pd.DataFrame()
df.iloc[6737617:6737617+1977]


# In[ ]:


df.head()


# In[ ]:


df.info()


# In[ ]:





# In[ ]:




