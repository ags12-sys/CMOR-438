# Data Sets

This folder contains the **datasets** used throughout the CMOR-438 project for both supervised and unsupervised learning tasks. Each dataset is used to demonstrate different machine learning algorithms, preprocessing techniques, and evaluation methods.

---

## 1. Wine Quality Dataset

- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Wine+Quality)  
- **File:** `winequality-red.csv`  
- **Description:** Contains chemical properties of red wine samples along with a quality score (0–10).  
- **Number of Instances:** 1,599  
- **Number of Features:** 11 chemical properties (e.g., acidity, sugar, alcohol) + 1 target variable (`quality`)  

### Usage in Notebooks
- **Classification tasks:** High vs. low wine quality (binary), multi-class classification.  
- **Unsupervised tasks:** PCA, K-Means Clustering, DBSCAN.  
- **Preprocessing Notes:**  
  - Standardization of features is necessary for distance-based algorithms.  
  - Target variable may be binarized for classification tasks.  
  - No missing values in the dataset.

---

## 2. California Housing Dataset

- **Source:** [Scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html)  
- **Description:** Median house prices and demographic information for California districts.  
- **Number of Instances:** 20,640  
- **Number of Features:** 8 numeric features (e.g., median income, house age, average rooms, population) + 1 target (`MedianHouseValue`)  

### Usage in Notebooks
- **Regression tasks:** Linear Regression, Gradient Descent, Neural Networks, MLP.  
- **Preprocessing Notes:**  
  - Feature scaling is critical for gradient-based models and neural networks.  
  - Train-test splitting is applied to avoid data leakage.  
  - Outliers may affect model performance; standardization reduces this impact.

---

## Notes
- Both datasets are **publicly available** and included for reproducibility.  
- Each notebook references the dataset path or fetches it programmatically.  
- Preprocessing steps (scaling, splitting, binarization) are performed **inside the notebooks** to ensure reproducibility.


