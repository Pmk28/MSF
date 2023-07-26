import matplotlib.pyplot as plt
import pandas as pd

#databáze hráčů hrajících v NBA v jednotlivých sezónách
data = pd.read_csv("all_seasons.csv")

pistons = data[(data["team_abbreviation"] == "DET") & (data["season"] == "2003-04")]
lakers = data[(data["team_abbreviation"] == "LAL") & (data["season"] == "2003-04")]

fig,graphs = plt.subplots(1,2)

graphs[0].scatter(pistons["gp"],pistons["reb"],s=pistons["pts"])
graphs[0].set_xlabel("games played")
graphs[0].set_ylabel("rebounds per game")
graphs[0].set_title("Detroit Pistons")

graphs[1].scatter(lakers["gp"],lakers["reb"],s=lakers["pts"])
graphs[1].set_xlabel("games played")
graphs[1].set_ylabel("rebounds per game")
graphs[1].set_title("Los Angeles Lakers")

plt.show()
