import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Student marks dataset
# Input features: Study hours and Sleep hours
# Target labels: 1 (Pass) or 0 (Fail)
X = np.array([[5, 7], [2, 8], [3, 5], [8, 3], [10, 6], [6, 9]])
y = np.array([1, 0, 0, 1, 1, 1])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create a logistic regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print(X_test)
print(model.predict([[6, 5]]))


"""
In this example, we have a dataset with two input features:
 study hours and sleep hours, and the corresponding target labels (pass or fail).

We define the input features X as a 2D array, where each row represents a student,
and each column represents a feature. We also define the target labels y as a 1D array.

We split the data into training and testing sets using train_test_split().
Here, we use 80% of the data for training and 20% for testing, with a random state of 42 for reproducibility.

We create a logistic regression model using LogisticRegression().

We train the model using the fit() method by passing the 
training set features X_train and target labels y_train.

After training, we predict the target labels for the test 
set using the predict() method and pass the test set features X_test.

We calculate the accuracy of the model by comparing the 
predicted labels y_pred with the true labels y_test using the accuracy_score() function.

Finally, we print the accuracy to see how well the logistic 
regression model performs in predicting whether a student will pass or fail
based on their marks (study hours and sleep hours).





"""
