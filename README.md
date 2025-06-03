## Fabric Quality Classification using Machine Learning

This project aims to classify fabric samples into quality levels (1st, 2nd, 3rd) based on various physical and structural properties using machine learning techniques — particularly a Random Forest Classifier.

---

## Problem Statement

In textile R&D, predicting fabric quality early based on objective test data (such as tensile strength, shrinkage, and elasticity) can save time, reduce waste, and support standardization. This project builds a predictive model that uses fabric attributes to estimate the quality class.

---

## Dataset Description

The dataset contains 300 synthetic samples generated for experimentation, each with the following features:

- `gramaj`: Fabric weight (g/m²)
- `cekme`: Shrinkage after washing (%)
- `mukavemet`: Tensile strength (N)
- `esneme`: Elongation (%)
- `opaklik`: Opacity (0-1)
- `elyaf_cinsi`: Type of fiber (e.g., Cotton, Polyester)
- `orgu_tipi`: Knitting type
- `dokuma_tipi`: Weaving type
- `kalite_turu`: Target label (1. kalite, 2. kalite, 3. kalite)

---

## Feature Engineering

To improve model performance, the following derived features were added:

- `mukavemet_per_gramaj`: Strength per gram
- `cekme_esneme_indeksi`: A combined measure of shrinkage and elasticity

Categorical features were encoded using **One-Hot Encoding** and numerical features were scaled using **MinMaxScaler**.

---

## Model

- **Model Used**: RandomForestClassifier (from `sklearn.ensemble`)
