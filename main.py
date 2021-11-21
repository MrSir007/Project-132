import csv
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans as km
import matplotlib.pyplot as plt
import seaborn as sns

rows = []
with open ("final.csv", "r") as fetchData :
  data = csv.reader(fetchData)
  for r in data :
    rows.append(r)

header = rows[0]
planetData = rows[1:]
header[0] = "no"
planetData = list(planetData)
# No need to convert into SI units, data already converted

planetMass = []
planetRadius = []
planetName = []
for i in planetData :
  planetMass.append(float(i[3])*1.989e+30)
  planetRadius.append(float(i[4])*float(i[4])*6.957e+8)
  planetName.append(i[1])

planetGravity = []
for index, name in enumerate(planetName) :
  gravity = planetMass[index] / planetRadius[index]
  planetGravity.append(gravity)
planetData.append(planetGravity)

plt.figure(figsize=(10,5))
sns.lineplot(planetMass, planetRadius, marker='o', color='green')
plt.title('Planets')
plt.xlabel('Mass')
plt.ylabel('Radius')
plt.show()

'''plt.figure(figsize=(10,5))
sns.lineplot(planetMass, planetGravity, marker='o', color='green')
plt.title('Planets')
plt.xlabel('Mass')
plt.ylabel('Gravity')
plt.show()'''