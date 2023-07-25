import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("world-data-2023.csv")
abr = ["CZ","KP","RU","US"]

countries = data[data["Abbreviation"].isin(abr)]
army_size = []


for i in [44,127,143,186]:
    countries.at[i,"Armed Forces size"] = countries.at[i,"Armed Forces size"].replace(",","")


for country in countries["Armed Forces size"]:
    army_size.append(float(country))

labels = ["Czech Republic", "North Korea", "Russia", "United States"]

plt.pie(army_size,labels=labels,autopct='%1.1f%%')
plt.title("Armed Forces Size")
plt.show()
