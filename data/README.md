# Dataset Directory & Pre-Trained Weights

This directory stores model artifacts and sample transactions for the Credit Card Fraud Detection research project.

## 1. Pre-Trained NumPy Model Weights (model_weights.npz)
To allow notebooks and tests to execute immediately without re-training models, pre-computed weights for all 6 from-scratch NumPy algorithms are serialized here (model_weights.npz).

## 2. Sample Verification Cases (sample_cases.json)
Contains 20 verified test transactions (10 fraud cases, 10 genuine cases) extracted from held-out splits for quick interactive testing and verification.

## 3. Downloading Raw Kaggle Dataset (creditcard.csv)
If you wish to re-train models from scratch on the raw dataset:
1. Download creditcard.csv from Kaggle: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
2. Place creditcard.csv directly into this data/ folder.
3. The dataset contains 284,807 transactions with 492 frauds (0.172% class imbalance) across 28 PCA features (V1 to V28) and Amount.
