import matplotlib.pyplot as plt
import pandas as pd

#databáze hráčů hrajících v NBA v jednotlivých sezónách
data = pd.read_csv("all_seasons.csv")

#selectuji data pouze o těchto dvou legendárních hráčích
kobe = data[(data["player_name"] == "Kobe Bryant")]
lebron = data[(data["player_name"] == "LeBron James")]

plt.plot(kobe["age"],kobe["pts"],color="yellow",label="Kobe Bryant")
plt.plot(lebron["age"],lebron["pts"],color="purple",label="LeBron James")
plt.title("Comparison of Kobe Bryant and LeBron James")
plt.xlabel("age")
plt.ylabel("points per game")
plt.legend()
plt.show()
