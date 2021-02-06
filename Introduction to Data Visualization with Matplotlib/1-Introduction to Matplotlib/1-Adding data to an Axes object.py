# # So as i understand  datacamp created subplots to show multiple graph in one.
# # Found  out there were several ways to that

import pandas as pd
import matplotlib.pyplot as plt

# not defining fif or ax
seattle_weather = pd.read_csv("seattle_weather2.csv")
austin_weather = pd.read_csv("austin_weather.csv")

plt.plot(seattle_weather["MONTH"],seattle_weather["MLY-PRCP-NORMAL"])
plt.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])
plt.xlabel("Time (months)")
plt.ylabel("Precipitation (inches)")
plt.title("Weather patterns in Austin and Seattle")
plt.show()

# or defining fig or ax
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"],seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])
ax.set_xlabel("Time (months)")
ax.set_ylabel("Precipitation (inches)")
ax.set_title("Weather patterns in Austin and Seattle")
plt.show()

fig2 = plt.figure()
ax = fig2.add_subplot(111)
ax.plot(seattle_weather["MONTH"],seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])
plt.show()

fig2 = plt.figure()
ax = fig2.add_subplot(111)
plt.plot(seattle_weather["MONTH"],seattle_weather["MLY-PRCP-NORMAL"])
plt.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])
plt.show()

# or we can merge the data and plot it

merged_weather = seattle_weather.merge(austin_weather, on= "MONTH")
merged_weather[["MONTH", "MLY-PRCP-NORMAL_x","MLY-PRCP-NORMAL_y"]].plot(x="MONTH",rot =95)
plt.show()

seattle_weather = pd.read_csv("seattle_weather2.csv",index_col="MONTH")
austin_weather = pd.read_csv("austin_weather.csv",index_col="MONTH")

merged_weather = seattle_weather.merge(austin_weather, on= "MONTH")
merged_weather[[ "MLY-PRCP-NORMAL_x","MLY-PRCP-NORMAL_y"]].plot(rot=90)
plt.show()
