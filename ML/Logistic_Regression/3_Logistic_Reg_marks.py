import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Set the random seed for reproducibility
np.random.seed(42)

# Total number of students
total_students = 50

# Generate random marks between 0 and 80
marks = np.random.randint(low=0, high=81, size=total_students)

# Set the threshold for passing marks
passing_marks = 38

# Create labels based on marks
labels = np.where(marks >= passing_marks, 1, 0)

# # Create the dataset
# dataset = np.column_stack((marks,labels))
# print(dataset)

reshaped_marks = np.reshape(marks, (-1, 1))

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(reshaped_marks, labels, test_size=0.2, random_state=42)
print(y_test)
# Create a logistic regression model
model = LogisticRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


