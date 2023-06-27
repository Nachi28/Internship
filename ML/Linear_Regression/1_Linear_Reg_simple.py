# Example 1 (x+2 )

import numpy as np
from sklearn.linear_model import LinearRegression

# Sample input data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Predict the output for new data
new_data = np.array([[6], [7]])
predictions = model.predict(new_data)

# Print the predictions
for i, prediction in enumerate(predictions):
    print(f"Prediction {i+1}: {prediction}")