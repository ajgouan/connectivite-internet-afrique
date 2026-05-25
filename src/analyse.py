#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/internet_users.csv")

print(f"Dimensions : {df.shape[0]} lignes x {df.shape[1]} colonnes")
df.head()

#%%

print(df.columns.tolist())

#%%

print(df.isnull().sum())

#%%

pays_africains = [
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi",
    "Cameroon", "Cape Verde", "Central African Republic", "Chad", "Comoros",
    "Congo", "Democratic Republic of Congo", "Djibouti", "Egypt",
    "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia",
    "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho",
    "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania",
    "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria",
    "Rwanda", "Senegal", "Sierra Leone", "Somalia", "South Africa",
    "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda",
    "Zambia", "Zimbabwe"
]

df_afrique = df[df["Location"].isin(pays_africains)].copy()

print(f"Pays africains trouvés : {len(df_afrique)}")
print(df_afrique["Location"].unique())

#%%

df_afrique = df[df["Location"].isin(pays_africains)][["Location", "Rate (ITU)"]].copy()

df_afrique.columns = ["Pays", "Taux_Internet"]

df_afrique = df_afrique.dropna(subset=["Taux_Internet"])

print(f"Pays avec des données disponibles : {len(df_afrique)}")
print()
print(df_afrique.describe().round(2))

#%%
# Top 10 pays les plus connectes
top10 = df_afrique.nlargest(10, "Taux_Internet")
print("TOP 10 PAYS LES PLUS CONNECTES")
print(top10.to_string(index=False))

print()

# Position de la Cote d'Ivoire
ci = df_afrique[df_afrique["Pays"] == "Ivory Coast"]
rank = df_afrique["Taux_Internet"].rank(ascending=False)[ci.index[0]]
print(f"Pays : COTE D'IVOIRE")
print(f"Taux : {ci['Taux_Internet'].values[0]}%")
print(f"Classement : #{int(rank)} sur {len(df_afrique)} pays")
print(f"Ecart avec la moyenne : {ci['Taux_Internet'].values[0] - 42.47:+.1f}% de la moyenne africaine")

#%%

moyenne = df_afrique["Taux_Internet"].mean()

plt.figure(figsize=(12, 6))

colors = ["#E85C1A" if pays == "Ivory Coast" else "#2E4057" for pays in top10["Pays"]]

bars = plt.barh(top10["Pays"], top10["Taux_Internet"], color=colors)

plt.axvline(moyenne, color="gray", linestyle="--", linewidth=1.5, label=f"Moyenne Afrique ({moyenne:.1f}%)")

plt.xlabel("Taux de penetration internet (%)")
plt.title("Top 10 pays africains les plus connectés")
plt.legend()
plt.xlim(0, 100)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

#%%

df_sorted = df_afrique.sort_values("Taux_Internet", ascending=True)

colors = ["#E85C1A" if pays == "Ivory Coast" else "#2E4057" for pays in df_sorted["Pays"]]

plt.figure(figsize=(12, 14))
plt.barh(df_sorted["Pays"], df_sorted["Taux_Internet"], color=colors)
plt.axvline(moyenne, color="gray", linestyle="--", linewidth=1.5, label=f"Moyenne Afrique ({moyenne:.1f}%)")
plt.xlabel("Taux de penetration internet (%)")
plt.title("Connectivité internet en Afrique — tous les pays")
plt.legend()
plt.xlim(0, 100)
plt.tight_layout()
plt.show()

#%%

plt.figure(figsize=(10, 5))

plt.hist(df_afrique["Taux_Internet"], bins=10, color="#2E4057", edgecolor="white")
plt.axvline(moyenne, color="#E85C1A", linestyle="--", linewidth=2, label=f"Moyenne ({moyenne:.1f}%)")
plt.axvline(df_afrique["Taux_Internet"].median(), color="gray", linestyle="--", linewidth=2, label=f"Mediane ({df_afrique['Taux_Internet'].median():.1f}%)")

plt.xlabel("Taux de penetration internet (%)")
plt.ylabel("Nombre de pays")
plt.title("Distribution de la connectivite en Afrique")
plt.legend()
plt.tight_layout()
plt.show()

# %%
