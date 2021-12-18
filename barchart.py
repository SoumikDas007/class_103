import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
bar=px.bar(df,x="Country",y="InternetUsers")
bar.show()