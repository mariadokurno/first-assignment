df = pd.read_csv("./train.tsv", sep='\t', names=["Cena",  "Ile_pokoi",  "Metraz", "Pietro", "Dzielnica", "Opis"])
description = pd.read_csv("./description.csv", header=0, names=["pietra", "opis_pietra"])
description

new_df = df.merge(description, left_on='Pietro', right_on='pietra', how='left')
new_df

new_df2 = new_df.loc[:, new_df.columns != 'pietra']
new_df2

new_df2.to_csv("out2.csv")
