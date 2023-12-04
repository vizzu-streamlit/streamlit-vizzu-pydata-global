# Welcome to Vizzu + Streamlit!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pydata-global.streamlit.app/)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://share.streamlit.io/create-from-fork?owner=blackary&repository=streamlit-vizzu-pydata-global&branch=main&mainModule=streamlit_app.py)

# Make your own fork of this app in Codespaces

Step 1:  Right click the "Open in Github Codespaces" button above, open the link in a new tab and then click Fork!

![image](https://github.com/blackary/streamlit-vizzu-pydata-global/assets/4040678/f4a9d972-cae6-4aa2-8b9a-2e18f513759a)

_(Eat a 🍪 while you wait)_

Step 2: Press "Create new Codespace"

<img width="521" alt="image" src="https://github.com/blackary/streamlit-vizzu-pydata-global/assets/4040678/87d24ecc-daf2-4292-a0fa-13e6fc68094e">

_(Check your bluesky while you wait)_

Step 3: After a minute or two, you should see an editor (it may take a few seconds after the page has loaded), and then a browser should open to the right (You can resize the site to see the whole app better)

<img width="1684" alt="image" src="https://github.com/blackary/streamlit-vizzu-pydata-global/assets/4040678/04f1be56-7b71-4303-81f0-ed7679e4b1a0">

# Add your own charts

Step 1: Download one of the csvs above in this repository

Step 2: In a new tab, open https://vizzu-builder.streamlit.app/ and upload the CSV you just downloaded.

Step 3: Choose 1 Category and one or more Values columns and hit `Create Charts` to see the different kinds of charts you can make.

<img width="825" alt="image" src="https://github.com/blackary/streamlit-vizzu-pydata-global/assets/4040678/868d5ac9-dafd-4fd2-af42-4a05873e81c7">

Step 4: Pick a chart you like and expand the "Show code" expander and press the Copy button at the top right of the section.

<img width="519" alt="image" src="https://github.com/blackary/streamlit-vizzu-pydata-global/assets/4040678/1b3f24c7-b88a-4d08-a4e2-1a127e26eca4">

Step 5: Go back to the Codespaces instance, and add a new file in the pages/ folder called `my_chart.py`.

<img width="330" alt="image" src="https://github.com/blackary/streamlit-vizzu-pydata-global/assets/4040678/47c3d21e-15bd-4e2a-a86c-4fbe70b939f6">

Step 6: Paste the code for your chart into the new file and save it. Re-run your app by pressing `r`. You should now see a new entry in the sidebar of your app

<img width="861" alt="image" src="https://github.com/blackary/streamlit-vizzu-pydata-global/assets/4040678/e91dfd7b-4832-42df-a36a-c0b4d8929f27">

Step 7: Take a look at the code for "pages/racing.py" to see how you can make your chart dynamically transform with streamlit widgets, and have fun!

```python
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
```
