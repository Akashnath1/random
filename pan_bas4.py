import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 500)
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

housing_data = pd.read_pickle('HPI.pickle')
housing_data = housing_data.pct_change()
print(housing_data)