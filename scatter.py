import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
scatter=px.scatter(df,x="Population",y="Per capita",size="Percentage",color="Country",size_max=100)
scatter.show()