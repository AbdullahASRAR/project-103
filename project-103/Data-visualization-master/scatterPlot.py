import pandas as pd

import plotly.express as px

df=pd.read_csv("data.csv")
fig=px.scatter(df,y="Per capita",x="Population",color="Country",size="Percentage")
fig.show()
