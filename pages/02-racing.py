from streamlit_vizzu import VizzuChart, Data, Config, Style

import streamlit as st
import pandas as pd

df = pd.read_csv("sales.csv")
data = Data()
data.add_df(df)

chart = VizzuChart()
chart.animate(data)

chart.animate(
	#Data.filter(f"record['Year'] == df['Year'].min()")
    Config(
        {
            "x": "Revenue[$]",
            "y": "Country",
			"label": "Revenue[$]",
        }
    ),
	Style({
        "plot": {
			"yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
			"xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
			"marker": {
				"label": {
					"numberFormat": "prefixed",
					"maxFractionDigits": "1",
					"numberScale": "shortScaleSymbolUS",
				},
			}
		}
	}),
    delay="0"
)

st.title("Sales by country")

config = {}
if st.toggle("Order by total"):
    config["sort"] = "byValue"
else:
    config["sort"] = "none"

year = st.slider(
    "Year",
    min_value=df["Year"].min(),
    max_value=df["Year"].max(),
    value=df["Year"].min(),
    step=1,
)

filter = Data.filter(f"record['Year'] == {year}")

chart.animate(Config(config), filter, delay="0", x={"easing": "linear"}, )

chart.show()
