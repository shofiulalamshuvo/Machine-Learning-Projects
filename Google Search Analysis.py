#importing_libraries
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

#importing_data
trends.build_payload(kw_list=["Machine Learning"])
data = trends.interest_by_region()
data = data.sort_values(by="Machine Learning", ascending=False)
data = data.head(15)
print(data)

#visualize_bar_chart
data.reset_index().plot(x="geoName", y="Machine Learning", figsize=(20,15), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()
