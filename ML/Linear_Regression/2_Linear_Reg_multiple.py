# Example 2 (a+b)

import numpy as np
from sklearn.linear_model import LinearRegression

# Sample input data
X = np.array([[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]])
y = np.array([3, 6, 9, 12, 15])

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Predict the output for new data
new_data = np.array([[6, 12], [7, 14]])
predictions = model.predict(new_data)

# Print the predictions
for i, prediction in enumerate(predictions):
    print(f"Prediction {i+1}: {prediction}")