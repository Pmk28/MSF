import matplotlib.pyplot as plt
import pandas as pd

#databáze hráčů hrajících v NBA v jednotlivých sezónách
data = pd.read_csv("all_seasons.csv")

season = data[(data["season"] == "2021-22")]

usa = 0
canada = 0
serbia = 0
france = 0

#vypočítám kolik hračů je z těchto zemí
for i in season["country"]:
    if i == "USA":
        usa += 1
    elif i == "Canada":
        canada += 1
    elif i == "Serbia":
        serbia += 1
    elif i == "France":
        france += 1

countries = [usa, canada, serbia, france]
names = ["USA","Canada","Serbia","France"]

plt.pie(countries,labels=names,autopct='%1.1f%%')
plt.title("Percentages of NBA players by these countries")
plt.show()
