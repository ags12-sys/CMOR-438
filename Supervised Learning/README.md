## Supervised Learning

The **Supervised Learning** section of this repository explores a wide range of **machine learning algorithms** for both **classification** and **regression** tasks. Supervised learning is a core branch of machine learning where models are trained using **labeled data**, learning to map input features to target outputs.  

This section uses two real-world datasets:  

- **Wine Quality Dataset** (Red Wine Chemical Properties)
  - Task: Classifying wine quality as high or low based on chemical measurements.
  - Challenges: Class imbalance and non-linear relationships between features.
- **California Housing Dataset**
  - Task: Predicting median house prices in California districts.
  - Challenges: High-dimensional numerical features, correlation between features, and outliers.

---

### Algorithms Implemented

1. **Perceptron**
   - Linear classifier for binary classification.
   - Demonstrates weight updates and convergence using the Perceptron learning rule.
   - Highlights the limitations of linear classifiers on non-linearly separable data.

2. **Gradient Descent**
   - Optimization algorithm to minimize a loss function iteratively.
   - Illustrated with both regression and classification examples.
   - Includes visualizations of loss convergence and effects of learning rate.

3. **Linear Regression**
   - Predicts continuous target values (California Housing prices).
   - Includes evaluation metrics: RMSE, Mean Absolute Error, and R².
   - Demonstrates multicollinearity issues and the effect of feature scaling.

4. **Logistic Regression**
   - Probabilistic binary classifier for Wine Quality.
   - Uses the sigmoid activation to model probability of class membership.
   - Shows decision boundaries and importance of regularization to prevent overfitting.

5. **Neural Networks (from scratch)**
   - Single-layer feedforward network.
   - Implements forward and backward propagation manually.
   - Demonstrates weight updates, learning rate tuning, and the effect of feature scaling.

6. **Multilayer Perceptron (MLP)**
   - Deep feedforward network with multiple hidden layers.
   - Capable of learning complex, non-linear relationships.
   - Includes ReLU/Sigmoid activations, weight initialization, and training monitoring.

7. **K-Nearest Neighbors (KNN)**
   - Distance-based, non-parametric classification.
   - Highlights the effect of feature scaling and choice of k on performance.
   - Sensitive to noise and irrelevant features, demonstrating the importance of preprocessing.

8. **Decision Trees**
   - Recursive, tree-based model that splits features to minimize impurity.
   - Easy to interpret and visualize.
   - Can overfit small datasets without depth or leaf restrictions.

9. **Ensemble Methods**
   - Combines multiple weak learners (bagging) for robust predictions.
   - Reduces variance and improves generalization.
   - Includes tests to verify reproducibility and estimator aggregation.

10. **Random Forest**
    - Ensemble of decision trees using bootstrapped samples and feature randomness.
    - Provides feature importance measures and robust predictions.
    - Handles high-dimensional data well and reduces overfitting compared to a single tree.

---

### Features & Highlights

- **Data Preprocessing**
  - Train-test splitting with stratification for classification tasks.
  - Feature scaling applied to distance-based or gradient-based models.
  - Target variable binarization for Wine Quality classification.
  - Handling of missing data (if present) and normalization where appropriate.

- **Model Training & Evaluation**
  - Step-by-step fitting and prediction for all models.
  - Evaluation metrics include accuracy, confusion matrix, classification reports, R², RMSE, and MAE.
  - Visualizations of training process: loss convergence, feature importance, decision boundaries.

- **Testing & Reproducibility**
  - Inline assertions in each notebook validate shapes, reproducibility, and correctness.
  - Ensures models produce consistent results and avoids silent errors.

- **Insights & Discussion**
  - Each notebook concludes with a **Summary & Discussion** highlighting:
    - Model performance and limitations
    - Insights about feature importance
    - Implications for dataset-specific tasks
    - Recommendations for further improvement
  
---

### Practical Notes

- Feature scaling is **critical** for KNN, Gradient Descent, and Neural Networks to ensure convergence and meaningful distance calculations.
- Random Forests and Decision Trees are **scale-invariant**, making them robust to unscaled features.
- Inline testing provides confidence that models are implemented correctly, reproducible, and maintainable.
