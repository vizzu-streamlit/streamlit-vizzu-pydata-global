from streamlit_vizzu import VizzuChart, Data, Config

import streamlit as st
import pandas as pd

df = pd.read_csv("sales.csv")
data = Data()
data.add_df(df)

chart = VizzuChart()
chart.feature("tooltip", True)
chart.animate(data)

chart.animate(
    Data.filter(None),
    Config(
        {
            "coordSystem": "cartesian",
            "geometry": "rectangle",
            "x": "Revenue[$]",
            "y": {"set": "Country"},
            "orientation": "vertical",
        }
    ),
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

chart.animate(Config(config), filter)

chart.show()
