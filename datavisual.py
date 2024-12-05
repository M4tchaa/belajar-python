import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
# Unvariate

## BAR - Category
cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yogyakarta', 
          'Surakarta','Surabaya', 'Medan', 'Makassar')
 
populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
               3481, 287750, 785409)
 
# plt.bar(x=cities, height=populations) #Vertical
# plt.xticks(rotation=45) #dibikin miring
# plt.show()

# plt.barh(y=cities, width=populations) #Horizontal
# plt.show()

#Diurutkan pake pandas
# df = pd.DataFrame({
#     'Cities': cities,
#     'Population': populations,
# })
 
# df.sort_values(by='Population', inplace=True)
 
# plt.barh(y=df["Cities"], width=df["Population"])
# plt.xlabel("Population (Millions)") #Tambahin keterangan
# plt.title("Population of Cities in Indonesia")
# plt.show()

## PIE - Category
flavors = ('Chocolate', 'Vanilla', 'Matcha', 'Others')
votes = (50, 20, 30, 10)
colors = ('#8B4513', '#FFF8DC', '#93C572', '#E67F0D')
explode = (0.02, 0, 0, 0)
 
# plt.pie(
#     x=votes, #tampungan data
#     labels=flavors, #isi data string
#     autopct='%1.1f%%', #ngasih numerik
#     colors=colors, #yaa warna tiap label (berurutan)
#     # explode=explode #tampungan array (Op wedgepros)
#     wedgeprops = {'width': 0.4} # donut (Op Explode)
# )
# plt.show()

## Histogram - Numerical
x = np.random.normal(15, 5, 250)
 
# plt.hist(x=x, bins=15)
# plt.show()

## Boxplot - Numerical
# y = np.random.normal(15, 5, 250)
# sns.boxplot(y)
# plt.show()

# LINE CHART
# lemon_diameter = [6.44, 6.87, 7.7, 8.85, 8.15, 
#                   9.96, 7.21, 10.04, 10.2, 11.06]
# lemon_weight = [112.05, 114.58, 116.71, 117.4, 128.93, 
#                 132.93, 138.92, 145.98, 148.44, 152.81]
 
# plt.plot(lemon_diameter, lemon_weight)
# plt.show()

# BCA with Linechart
# url = 'https://query1.finance.yahoo.com/v7/finance/download/BBCA.JK?period1=1644796800&period2=1676332800&interval=1d&events=history&includeAdjustedClose=true'
# df = pd.read_csv(url)
# df['Date'] = pd.to_datetime(df['Date'])
 
# plt.figure(figsize=(12, 5))
# plt.plot(df['Date'], df['Close'], color='red')
# plt.xlabel('Date',size=15)
# plt.ylabel('Price',size=15)
# plt.show()

# BarPLOT
# penguins = sns.load_dataset("penguins")
 
# sns.barplot(data=penguins, x="species", y="body_mass_g", hue="sex", errorbar=None)
# plt.show()

###Explanatori Data = Cerita dari DATA
# url = 'https://query1.finance.yahoo.com/v7/finance/download/BBCA.JK?period1=1644796800&period2=1676332800&interval=1d&events=history&includeAdjustedClose=true'
# df = pd.read_csv(url)
# df['Date'] = pd.to_datetime(df['Date'])
 
# plt.figure(figsize=(12, 5))
# plt.plot(df['Date'], df['Close'], label='Close', color='red')
# plt.plot(df['Date'], df['Open'], label='Open', color='blue')
# plt.title('BBCA Stock Price', size=20)
# plt.xlabel('Date',size=15)
# plt.ylabel('Price (IDR)',size=15)
# plt.legend()
# plt.show()

#Contoh Implementasi Kontras Biar JAga Fokus Audience
# penguins_df = sns.load_dataset("penguins")
 
# adelie_df = penguins_df[penguins_df.species == "Adelie"]
# chinstrap_df = penguins_df[penguins_df.species == "Chinstrap"]
# gentoo_df = penguins_df[penguins_df.species == "Gentoo"]
 
# plt.figure(figsize=(10, 5))
# sns.scatterplot(data=adelie_df, x="body_mass_g", y="flipper_length_mm", facecolor="lightgrey", label="Adelie")
# sns.scatterplot(data=chinstrap_df, x="body_mass_g", y="flipper_length_mm", facecolor="lightgrey", label="Chinstrap")
# sns.scatterplot(data=gentoo_df, x="body_mass_g", y="flipper_length_mm", facecolor="blue", label="Gentoo")
# plt.legend()
# plt.show()