# -*- coding: utf-8 -*-
"""Colab'e hoş geldiniz.

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb

# Değerlerine göre kumaş kalitesi analizi
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('Kumas_Kalite_Verisi.csv')
df.head(3)

df.columns

df.info()

df.describe()

df.isnull().sum()

cols = ['elyaf_cinsi', 'orgu_tipi', 'dokuma_tipi']


for col in cols:
    df[col] = df[col].astype(str).str.lower()


print(df[['elyaf_cinsi', 'orgu_tipi', 'dokuma_tipi']].head())

df_encoded = pd.get_dummies(df,
                            columns=["elyaf_cinsi", "orgu_tipi", "dokuma_tipi"],
                            drop_first=True,
                            dtype=int)
df_encoded.head(3)

df_encoded["mukavemet_per_gramaj"]=df["mukavemet"] / df["gramaj"]

df_encoded["cekme_esneme_indeksi"]=df["cekme"] * df["esneme"]

from sklearn.preprocessing import MinMaxScaler

numerics = ["gramaj", "cekme", "mukavemet", "esneme", "opaklik", "cekme_esneme_indeksi"]
scaler = MinMaxScaler()
df_encoded[numerics] = scaler.fit_transform(df_encoded[numerics])

from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()
df_encoded["kalite_turu_encoded"] = le.fit_transform(df["kalite_turu"])

x=df_encoded.drop(["kalite_turu", "kalite_turu_encoded"],axis=1)
y=df_encoded["kalite_turu_encoded"]

plt.figure(figsize=(8,5))
sns.boxplot(x="kalite_turu", y="mukavemet", data=df)
plt.title("Kalite Türüne Göre Mukavemet Grafiği")
plt.show()

"""**Random Forest Classifier**"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

X = df_encoded.drop(["kalite_turu", "kalite_turu_encoded"], axis=1)
y = df_encoded["kalite_turu_encoded"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)

print(" Doğruluk (Accuracy):", accuracy_score(y_test, y_pred))
print("\n Sınıflandırma Raporu:\n", classification_report(y_test, y_pred, target_names=le.classes_))

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=le.classes_, yticklabels=le.classes_)
plt.xlabel("Tahmin")
plt.ylabel("Gerçek")
plt.title("Confusion Matrix - Random Forest")
plt.tight_layout()
plt.show()

"""Modelin hangi değişkenlere ne kadar önem verdiğini görmek"""

feature_importances = pd.Series(rf_model.feature_importances_, index=X.columns)
feature_importances.nlargest(10).plot(kind='barh')
plt.title("Random Forest - Öznitelik Önemi")
plt.xlabel("Öznitelik Önemi")
plt.tight_layout()
plt.show()