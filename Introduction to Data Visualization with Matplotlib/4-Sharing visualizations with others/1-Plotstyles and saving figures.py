import pandas as pd
import matplotlib.pyplot as plt

austin_weather = pd.read_csv("austin_weather.csv")
seattle_weather = pd.read_csv("seattle_weather2.csv")

plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
# we can set figure size
fig.set_size_inches([3,5])
plt.show()

# we can also  save the grapg as png
fig.savefig("graph.png")

plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
fig.set_size_inches([5,3])
plt.show()
fig.savefig("graph300.png", dpi=300)





