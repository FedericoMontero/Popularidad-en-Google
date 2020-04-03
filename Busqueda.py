from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
pytrends.build_payload(['Coronavirus'], cat=0, timeframe='2020-02-01 2020-03-20',  gprop='', geo='UY')

df = pytrends.interest_over_time()
print(df.head())

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set()
df['timestamp'] = pd.to_datetime(df.index)
sns.lineplot(df['timestamp'], df['Coronavirus'])
plt.title("Busquedas en Uruguay")
plt.ylabel("Numero de Busuqedas")
plt.xlabel("Fecha")
