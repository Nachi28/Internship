import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


# Read the data from CSV file
df = pd.read_csv('ML\Linear_Regression\house_data.csv')

# Extract the independent variables (house size, number of bedrooms, and distance to city center)
X = df[['House Size (in sq. ft.)', 'Number of Bedrooms',
        'Distance to City Center (in km)']]
# Extract the dependent variable (price)
y = df['Price (in ₹1000s)']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create and fit the linear regression model using the training data
regression = LinearRegression()
regression.fit(X_train, y_train)

# Predict the prices for the testing data
y_pred = regression.predict(X_test)

# Plot the actual and predicted prices for the testing data
# plt.scatter(y_test, y_pred)
# plt.xlabel('Actual Price (in ₹1000s)')
# plt.ylabel('Predicted Price (in ₹1000s)')
# plt.title('Actual vs Predicted Prices (Testing Data)')
# plt.show()

# Plot the scatter plot of actual data
plt.scatter(X_test['House Size (in sq. ft.)'], y_test, label='Actual')
# Plot the linear regression line
plt.plot(X_test['House Size (in sq. ft.)'], y_pred,
         color='red', linewidth=2, label='Predicted')
plt.xlabel('House Size (in sq. ft.)')
plt.ylabel('Price (in ₹1000s)')
plt.title('House Price vs. Size with Linear Regression')
plt.legend()
plt.show()

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
