import pandas as pd
import numpy as np

data = [
    {"Name": "Nelson", "Country": "Espana", "City": "Caceres"},
    {"Name": "David", "Country": "UK", "City": "London"},
    {"Name": "John", "Country": "Sweden", "City": "Stockholm"}
]

df = pd.DataFrame(data)

wights = [74, 78, 69]
heights = [179, 175, 169]
df['Weight'] = wights
df['Height'] = heights
df['Height'] = df['Height'] * 0.01

def calcular_bmi():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w, h in zip(weights, heights):
        b  = w / (h * h)
        bmi.append(b)
    return bmi
bmi = calcular_bmi()
df['BMI'] = bmi
df['BMI'] = round(df['BMI'], 1)

birth_years = [1982, 1985, 1990]
current_years = 2025

df['Birth Year'] = birth_years

df['Birth Year'] = pd.to_numeric(df['Birth Year'])

df['Age'] = current_years - df['Birth Year']

print(df)
