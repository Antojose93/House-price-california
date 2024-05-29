import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# Load data
data = pd.read_csv("housing.csv", delimiter=",")

# One-hot encode categorical variable
dummies = pd.get_dummies(data["ocean_proximity"], dtype=int)
data = data.join(dummies)

# Filter to adjust to reality
data = data[(data['housing_median_age'] < 50) & (data["median_income"] < 15.0)]
data.drop(["ocean_proximity"], axis=1, inplace=True)

# Impute missing values
imputer = SimpleImputer(strategy="median")
data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

# Drop rows with missing values
data = data.dropna()

# Function to predict house price
def predict_price(model, input_data):
    prediction = model.predict(input_data)
    return prediction

# Main function of the app
def main():
    st.title("California House Price Prediction")

    st.write("This app predicts the median price of houses in California based on the information availible on Kaggle.")

    st.subheader("House Data")
    st.write(data)

    st.subheader("Model Training")
    X = data.drop(["median_house_value"], axis=1)
    y = data["median_house_value"]
    model = LinearRegression()
    model.fit(X, y)
    
    # Interface to input house data for prediction
    st.subheader("Enter the house data to predict its price:")
    housing_median_age = st.number_input("Median House Age", min_value=1)
    median_income = st.number_input("Median Income", min_value=0.0, max_value=15.0, step=0.1)
    total_rooms = st.number_input("Total Rooms", min_value=0)
    total_bedrooms = st.number_input("Total Bedrooms", min_value=0)
    population = st.number_input("Population", min_value=3, max_value=35682)
    households = st.number_input("Households", min_value=0)
    latitude = st.number_input("Latitude", min_value=32, max_value=41)
    longitude = st.number_input("Longitude", min_value=-124, max_value=-113)
    ocean_proximity_options = ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
    ocean_proximity = st.selectbox("Ocean Proximity", ocean_proximity_options)

    # Create input data including one-hot encoding
    data_input = [[longitude ,latitude, housing_median_age,total_rooms,total_bedrooms,  population, households, median_income ]]
    ocean_proximity_mapping = {
    "<1H OCEAN": 0,
    "INLAND": 1,
    "ISLAND": 2,
    "NEAR BAY": 3,
    "NEAR OCEAN": 4
    }

    # Initialize a list with zeros
    ocean_proximity_values = [0] * len(ocean_proximity_mapping)

    # Get the numerical value corresponding to the selected ocean proximity option
    ocean_proximity_value = ocean_proximity_mapping.get(ocean_proximity, -1)  # Default value of -1 if option not found

    # Set the value of the corresponding column to 1
    if ocean_proximity_value != -1:
        ocean_proximity_values[ocean_proximity_value] = 1

    # Extend the data_input list with the numerical values
    data_input[0].extend(ocean_proximity_values)

        # Convert to DataFrame
    input_df = pd.DataFrame(data_input, columns=X.columns)

    # Perform prediction
    if st.button("Predict"):
        predicted_price = predict_price(model, input_df)
        st.success(f"The predicted median house price is: ${predicted_price[0]:,.2f}")
        #print(input_df)

if __name__ == "__main__":
    main()
