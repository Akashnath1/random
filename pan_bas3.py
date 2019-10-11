import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 500)
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')



def state_list():
    stateslist  = pd.read_html('https://simple.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')
    # print(stateslist)
    # print(stateslist[0])
    df1 = pd.DataFrame(stateslist[0])
    df2 = pd.DataFrame(df1['postal abbreviation[1]'])
    return (df2['postal abbreviation[1]'][:])

def initial_data():
    states = state_list()
    main_df = pd.DataFrame()
    for abb in states:
        print(abb)
        query = "FMAC/HPI_" + str(abb)
        df = quandl.get(query, authtoken="vAUsBHDEPNUJCMaG7AoF")
        df ['NSA Value'] = (df['NSA Value'] - df['NSA Value'][0]) / df['NSA Value'][0] *100
        df ['NSA Value'] = (df['SA Value'] - df['SA Value'][0]) / df['SA Value'][0] *100
        # # print(abb)
        print(df.head(2))
        if main_df.empty:
            main_df = df
            main_df.rename(columns={'NSA Value':'NSA Value'+abb, 'SA Value':'SA Value'+abb}, inplace=True)
        else:
            # print(tex_hpi.join(us_hpi, on='Date', lsuffix='TEX', rsuffix='USA'))
            main_df = main_df.join(df, on='Date', rsuffix=abb)

    pickle_out = open('pandaspdata.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()


def usa_hpi():
    query = "FMAC/HPI_USA"
    df = quandl.get(query, authtoken="vAUsBHDEPNUJCMaG7AoF")
    return df

def tx_hpi():
    query = "FMAC/HPI_TX"
    df = quandl.get(query, authtoken="vAUsBHDEPNUJCMaG7AoF")
    return df

def hpi_pickling():
    pickle_in = open('statedata.pickle', 'rb')
    hp_data = pickle.load(pickle_in)
    # print(emp_data)
     #using pandas pickling
    hp_data.to_pickle('pandaspdata.pickle')



def mortgage_30y():
    df = quandl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken="vAUsBHDEPNUJCMaG7AoF")
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df=df.resample('1D').mean()
    df=df.resample('M').mean()
    return df

def sp500_data():
    df = quandl.get("MULTPL/SP500_DIV_MONTH", trim_start="1975-01-01", authtoken="vAUsBHDEPNUJCMaG7AoF")
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df=df.resample('M').mean()
    df.rename(columns={'Value':'sp500'}, inplace=True)
    df = df['sp500']
    return df

def gdp_data():
    df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken="vAUsBHDEPNUJCMaG7AoF")
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df=df.resample('M').mean()
    df.rename(columns={'Value':'GDP'}, inplace=True)
    df = df['GDP']
    return df

def us_unemployment():
    df = quandl.get("FRBC/UNEMP_ST_US", trim_start="1975-01-01", authtoken="vAUsBHDEPNUJCMaG7AoF")
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df=df.resample('1D').mean()
    df=df.resample('M').mean()
    return df



# initial_data()
# hp_states= pd.read_pickle('pandaspdata.pickle')
# print(hp_states)


def hpi_correlation():
    hpi_state_correlation = hp_states.corr()
    # print(hpi_state_correlation)
    # print(hpi_state_correlation.describe())
    return hpi_state_correlation

# hp_us = usa_hpi()
# hp_data.plot()
# plt.legend().remove()
# plt.show()

fig = plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1),(1,0), sharex=ax1)

# hp_states.plot(ax=ax1)
# hp_us.plot(ax=ax1, color='k', linewidth=10)
#
# plt.legend().remove()
# plt.show()
def hpi_resampling():
    tex_hpi = tx_hpi()
    tx_hp_yearly = tex_hpi.resample('A').mean()
    # print(tx_hp_yearly)
    # tex_hpi.plot(ax=ax1)
    # tx_hp_yearly.plot(ax=ax1, color='k')
    tex_hpi [['NSA YEARLY', 'SA YEARLY']] = tx_hp_yearly
    print(tex_hpi)
    tex_hpi.dropna(inplace=True)
    print(tex_hpi)
    tex_hpi.dropna(how='all', inplace=True)
    tex_hpi.fillna(method='ffill', inplace=True)
    tex_hpi.fillna(method='bfill', inplace=True)
    tex_hpi.fillna(value=-99999, inplace=True)
    # plt.legend().remove()
    # plt.show()

#
# tex_hpi = pd.DataFrame(tx_hpi())
# # us_hpi= pd.DataFrame(usa_hpi())
# # print(us_hpi)
# # print(tex_hpi.join(us_hpi, on='Date', lsuffix='TEX', rsuffix='USA'))
#
# tex_hpi[['NSA 12MEAN', 'SA 12MEAN']] = tex_hpi.rolling(12).mean()
# # tex_hpi12 = pd.DataFrame(tex_hpi12)
# # tex_hpi.dropna(inplace=True)
# tex_hpi[['NSA 12SD', 'SA 12SD']] = tex_hpi[['NSA Value', 'NSA 12MEAN']].rolling(12).std()
# # print(tex_hpi)
# # tex_hpi[['NSA Value', 'NSA 12MEAN']].plot(ax=ax1)
# # # tex_hpi12.plot(ax=ax1)
# # tex_hpi[['NSA 12SD', 'SA 12SD']].plot(ax=ax2)
#
# print(hp_states['NSA ValueNJ'])
# print(hp_states['NSA ValueNY'])
# # print(hp_states['NSA ValueNJ'].loc['19990131':'20010131'])
# # print(hp_states['NSA ValueNY'].loc['19990131':'20010131'])
# NJ_NY12corr = hp_states['NSA ValueNJ'].rolling(12).corr(hp_states['NSA ValueNY'])
# # NJ_NY12corr = hp_states['NSA ValueNY'].rolling(12).corr()
# print(NJ_NY12corr)
# hp_states['NSA ValueNJ'].plot(ax=ax1, label='NJ NSA')
# hp_states['NSA ValueNY'].plot(ax=ax1, label='NY NSA')
# NJ_NY12corr.plot(ax=ax2, label='12 CORR')
# ax1.legend(loc=4)
# plt.legend()
# plt.show()

#initial_data()
hp_states= pd.read_pickle('pandaspdata.pickle')

m30 = mortgage_30y()
sp500 = sp500_data()
gdp = gdp_data()
HPI_Bench = usa_hpi()
unemployment = us_unemployment()
m30.columns=['M30']
HPI = HPI_Bench.join([m30,sp500,gdp,unemployment])
HPI.dropna(inplace=True)
print(HPI)
print(HPI.corr())
HPI.to_pickle('HPI.pickle')