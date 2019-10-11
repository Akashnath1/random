import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
import quandl
import bs4

# mydf1 = quandl.get("UIFS/WAGE_POL",
#                    authtoken="vAUsBHDEPNUJCMaG7AoF")
# print(mydf1.tail())
# df1 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2, 3, 2, 2],
#                     'US_GDP_Thousands':[50, 55, 65, 55]},
#                    index = [2001, 2002, 2003, 2004])
#
# df2 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2, 3, 2, 2],
#                     'US_GDP_Thousands':[50, 55, 65, 55]},
#                    index = [2005, 2006, 2007, 2008])
#
# df3 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2, 3, 2, 2],
#                     'Low_tier_HPI':[50, 52, 50, 53]},
#                    index = [2001, 2002, 2003, 2004])
#
# # mydf1 = pd.concat([df1, df2, df3])
# # print(mydf1)
# mydf2 = df1.append(df3)
# print(mydf2)

# stateslist  = pd.read_html('https://simple.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')
# # print(stateslist)
# # print(stateslist[0])
# df = pd.DataFrame(stateslist[0])
# df2 = pd.DataFrame(df['Name &postal abbreviation[1]'])
# for abb in df2['Name &postal abbreviation[1].1']:
#     print(abb)

# df1 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2, 3, 2, 2],
#                     'US_GDP_Thousands':[50, 55, 65, 55]},
#                    index = [2001, 2002, 2003, 2004])
#
# df2 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2, 3, 2, 2],
#                     'US_GDP_Thousands':[50, 55, 65, 55]},
#                    index = [2005, 2006, 2007, 2008])
#
# df3 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Unemployment':[7, 8, 9, 6],
#                     'Low_tier_HPI':[50, 52, 50, 53]},
#                    index = [2001, 2002, 2003, 2004])
#
# merged1 = pd.merge(df1,df2, on='HPI')
# merged1.set_index('HPI', inplace=True)
# print(merged1)
#
# # df1.set_index('HPI', inplace=True)
# df3.set_index('HPI', inplace=True)
# merged2 = df1.join(df3)
# print(merged2)

df1 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })

df3 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})

# merged1 = pd.merge(df1, df3, on='Year', how='right')
# merged1 = pd.merge(df1, df3, on='Year', how='left')
# merged1 = pd.merge(df1, df3, on='Year', how='inner')
merged1 = pd.merge(df1, df3, on='Year', how='outer')
merged1.set_index('Year', inplace=True)
print(merged1)
