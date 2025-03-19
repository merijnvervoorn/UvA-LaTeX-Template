import matplotlib.pyplot as plt

# Load data
df_kabinetten = pd.read_csv('kabinetten_schoongemaakt.csv')

# analyse cabinet length
df_kabinets_duur = df_kabinetten.groupby(df_kabinetten['Aantreden'].str[:4].astype(int))['Dagen'].sum()

# Trends in cabinet length
plt.figure(figsize=(12, 8))
df_kabinets_duur.plot(kind='bar', color='skyblue')
plt.ylabel('Days')
plt.xlabel('Year')
plt.title('Duration per year')
plt.tight_layout()
plt.show()
