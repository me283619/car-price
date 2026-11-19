# Car Price Prediction

A Machine Learning web application built with **Gradio** and **Random Forest Regressor** to predict used car prices based on vehicle features and preprocessing artifacts.

## Overview
This project predicts car prices using a trained `RandomForestRegressor` model paired with per-column `TargetEncoder` transformations, `StandardScaler` scaling, and a saved feature list inside a single serialized bundle (`car_price_model.pkl`).

## Key Highlights
- **Model:** `RandomForestRegressor` with strong predictive performance ($R^2$ around `0.93–0.95`).
- **Preprocessing Pipeline:** Saved `TargetEncoder` dictionary for categorical columns, `StandardScaler` for numerical scaling, and ordered feature names.
- **Interactive UI:** Built using `gr.Blocks` with structured input controls and sample examples.
- **Artifact Size:** Compressed with `joblib.dump(..., compress=3)` to around `22.6 MB`.

## Project Structure
```text
car-price/
├── app.py                  # Gradio inference application
├── car_price.ipynb         # Experimentation, training, and evaluation notebook
├── car_price_model.pkl     # Serialized model, encoders, scaler, and feature list
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
