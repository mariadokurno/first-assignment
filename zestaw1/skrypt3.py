# 4

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', -1)

df_schema = pd.read_csv('survey_results_schema.csv')
df_schema

df_survey = pd.read_csv('survey_results_public.csv',
                        usecols=['Extraversion', 'CodeRevHrs', 'Age', 'ConvertedComp'],
                        index_col='Gender')


df_survey.dtypes
df_survey.info()

df_survey.shape
df_survey.dropna(inplace=True)
df_survey.shape

# 5

df_survey.Age.unique()
df_survey = df_survey[df_survey['Age'] >= 18]

df_survey.Extraversion.unique()
df_introvert = df_survey[(df_survey['Extraversion'] == 'Online') | (df_survey['Extraversion'] == 'Neither')]
df_extrovert = df_survey[df_survey['Extraversion'] == 'In real life (in person)']


plt.plot(df_introvert['Age'], df_introvert['ConvertedComp']/1000, 'bo', markersize=0.6)
plt.xlabel('Age')
plt.ylabel('ConvertedComp')
plt.title('Introvert')
plt.show()

plt.plot(df_extrovert['Age'], df_extrovert['ConvertedComp']/1000, 'bo', markersize=0.6)
plt.xlabel('Age')
plt.ylabel('ConvertedComp')
plt.title('Extrovert')
plt.show()
