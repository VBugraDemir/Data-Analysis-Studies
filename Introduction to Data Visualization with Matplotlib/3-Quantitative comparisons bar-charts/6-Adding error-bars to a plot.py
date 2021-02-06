import pandas as pd
import matplotlib.pyplot as plt

seattle_weather = pd.read_csv("seattle_weather2.csv")
austin_weather = pd.read_csv("austin_weather.csv")

fig, ax = plt.subplots()
ax.errorbar(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"], yerr=seattle_weather["MLY-TAVG-STDDEV"])
ax.errorbar(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"], yerr=austin_weather["MLY-TAVG-STDDEV"])
ax.set_ylabel("Temprature (Fahrenheit)")
plt.show()
