import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("world-data-2023.csv")



for i in range(195):
    data.at[i,"Density\n(P/Km2)"] = int(data.at[i,"Density\n(P/Km2)"].replace(",",""))

sel_data = data[data["Density\n(P/Km2)"] > 1000]
rem_data = sel_data[sel_data["Country"] != "Vatican City"]


plt.bar(rem_data["Country"],rem_data["GDP"])
plt.title("Countries with density over 1000(P/Km2)")
plt.xlabel("Countries")
plt.ylabel("GDP")
plt.show()
