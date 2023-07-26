import matplotlib.pyplot as plt
import pandas as pd

#databáze hráčů hrajících v NBA v jednotlivých sezónách
data = pd.read_csv("all_seasons.csv")

#selectuji pouze hráče s výškou nad 215 centimetrů, kteří hráli v nba v jedné z sezón 2010-11 až 2021-22
sel_data = data[(data["player_height"] > 215) & (data["season"].str.startswith("201"))]

plt.hist(sel_data["season"],edgecolor="red",color="black")
plt.title("Players above 215 centimeters")
plt.xlabel("Seasons")
plt.ylabel("Frequency")
plt.show()
