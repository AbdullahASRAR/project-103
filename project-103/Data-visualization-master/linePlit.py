import pandas as pd

import plotly.express as px

df=pd.read_csv("line_chart.csv")
fig=px.line(df,y="Per capita income",x="Year",color="Country")
fig.show()
