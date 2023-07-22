import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('london_weather.csv')

january_2020 = data[(data["date"] >= 20200101) & (data["date"] <= 20200131)]
custom_x = [f"{i}." for i in range(1,32)]

plt.figure(figsize=(10,10))
plt.bar(january_2020["date"],january_2020["max_temp"])
plt.title('January 2020 - London')
plt.xticks(january_2020["date"],custom_x)
plt.xlabel("Days")
plt.ylabel("Highest Temperature")
plt.show()
