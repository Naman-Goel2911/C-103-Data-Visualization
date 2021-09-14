import pandas as pd
import plotly.express as px

df = pd.read_csv('Data.csv')

fig = px.scatter(df, x='date', y='cases', title='Covid Cases Analysis', color='country')
fig.show()