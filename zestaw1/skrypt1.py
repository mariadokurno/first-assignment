
# 1

import pandas as pd

df = pd.read_csv("./train.tsv", sep='\t', names=["Cena",  "Ile_pokoi",  "Metraz", "Pietro", "Dzielnica", "Opis"])
df

df['Cena'] = df['Cena'] * 1000
avg_price = str(round(df['Cena'].mean()))
# average price is 341763

file = open("out0.csv", "w")
file.write(avg_price)
file.close()

# 2

df['Cena_za_metr2'] = round((df['Cena'] / df['Metraz']), 1)
df

avg_price = round(df['Cena_za_metr2'].mean())
# avg price for squared meter is 6253

df1 = df[['Ile_pokoi', 'Cena', 'Cena_za_metr2']][(df.Ile_pokoi >= 3) & (df.Cena_za_metr2 < avg_price)]
df1

df1.to_csv("out1.csv", header=0)
