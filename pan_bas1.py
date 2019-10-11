import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 500)

# import numpy as np
#
# data_stats = {'Roll_no': [1,2,3,4,5,6,7,8],
#               'Name':["Akash", "Ayush", "Nick", "Praneet", "Crap"
#                       , "Piy", "Diy", "Kiy"],
#               'Subject':["Eng","Hin", "Crap", "Rand","Ans",
#                          "Asdf","dggr", "gdtt"],
#               'Score': [23,45,24,56,44,34,78,35]
#              }
# mydf = pd.DataFrame(data_stats)
# print(mydf)
# print(mydf.head(2))
# print(mydf.head())
# print(mydf.tail(3))
# print(mydf.tail())
#
# # mydf.set_index('Name', inplace=True)
# # print(mydf)
# print(mydf[['Name', 'Score']])
# arr= np.array(mydf[['Name', 'Score']])
# print(arr)
# mydf2 = pd.DataFrame(arr)
# print(mydf2)
# mydf = pd.read_csv('data1.csv')
# print(mydf)
# mydf.set_index('Date', inplace=True)
# mydf.to_csv('newdata1.csv')
# mydf2 = pd.read_csv('FRED-EMPLOYTX.csv')
# print(mydf2)
# mydf2.rename(columns={'Datee':'Date'}, inplace=True)
# print(mydf2)
# mydf2.to_csv('data3.csv', header=False)
# mydf3 = pd.read_csv('data3.csv', names={'Date', 'Valueee'}, index_col=0)
# print(mydf3)

# bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}
# df = pd.DataFrame(bridge_height)
#
# df ['STD'] = df.rolling(2).std()
# # print(df)
# df_std = df.describe()['meters']['std']
# df = df [(df['STD'] < df_std)]
# print(df)
# df['meters'].plot()
# plt.show()
