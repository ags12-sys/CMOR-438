# Supervised Learning

Supervised learning is a machine learning paradigm where models are trained on labeled data, consisting of input features and corresponding target values. The objective is to learn a mapping function that generalizes well to unseen data.


Supervised learning is primarily used for:

-Classification (predicting discrete labels)

-Regression (predicting continuous values)


This repository implements and compares several classical and modern supervised learning algorithms, focusing on performance, interpretability, and scalability.

## Key Concepts

-Features (X): Input variables used for prediction

-Labels (y): Ground truth outputs

-Loss Function: Measures prediction error

-Optimization: Minimization of loss via parameter updates

-Generalization: Model performance on unseen data

## Algorithms Implemented
### Perceptron:

-Linear binary classifier

-Learns a separating hyperplane via misclassification-driven updates

-Foundation of modern neural networks

-Best suited for linearly separable data

### Gradient Descent:

-Iterative optimization algorithm

-Minimizes a differentiable loss function

-Used to train linear models and neural networks

-Variants include batch, stochastic, and mini-batch gradient descent

### Linear Regression:

-Models linear relationships between features and a continuous target

-Optimized using least squares or gradient descent

-Highly interpretable coefficients

-Common baseline for regression tasks

### Logistic Regression:

-Probabilistic linear classifier

-Uses the logistic (sigmoid) function for binary classification

-Can be extended to multiclass problems

-Widely used due to simplicity and interpretability

### Neural Networks:

-Composed of layers of interconnected neurons

-Capable of modeling complex, non-linear relationships

-Trained using backpropagation and gradient descent

-Applicable to both regression and classification

### K-Nearest Neighbors (KNN):

-Instance-based, non-parametric algorithm

-Predicts outcomes based on the k closest data points

-No explicit training phase

-Sensitive to feature scaling and distance metrics

### Decision Tree:

-Tree-based model using recursive feature splits

-Handles non-linear decision boundaries

-Easy to visualize and interpret

-Prone to overfitting without regularization

### Ensemble Methods:

-Combine multiple models to improve robustness

-Reduce variance and/or bias

-Common techniques include bagging and boosting

-Often outperform single models

### Multilayer Perceptron (MLP):

-Feedforward neural network with hidden layers

-Uses non-linear activation functions

-Can approximate complex functions

-General-purpose supervised learning model

### Random Forest:

-Ensemble of decision trees

-Uses bootstrapped samples and random feature selection

-Improves generalization and reduces overfitting

-Provides feature importance estimates

## Goals

-Compare supervised learning algorithms under consistent conditions

-Analyze trade-offs between interpretability and performance

-Demonstrate practical application of foundational ML techniques
