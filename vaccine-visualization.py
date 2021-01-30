import geopandas
import pandas as pd
import dash
from dash.dependencies import Input, Output

df = pd.read_csv('COVID-19_Vaccine_Distribution_Allocations_by_Jurisdiction_-_Pfizer.csv')
print(df.head(10))