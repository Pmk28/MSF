import matplotlib.pyplot as plt
import pandas as pd

#databáze hráčů hrajících v NBA v jednotlivých sezónách
data = pd.read_csv("all_seasons.csv")

#vyselectuji pouze hráče hrající v 2021-22 season, kteří skórovali více než 28 bodů na zápas
season = data[(data["season"] == "2021-22") & (data["pts"] > 28)]

plt.bar(season["player_name"],season["pts"])
plt.title("NBA players who averaged over 28 points per game (2021-22)")
plt.ylabel("points per game")
plt.xlabel("players")
plt.show()
