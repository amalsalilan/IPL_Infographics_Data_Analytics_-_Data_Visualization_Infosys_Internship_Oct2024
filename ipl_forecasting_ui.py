import streamlit as st
import pickle
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Load the trained model (ipl_forecasting.pkl)
with open('ipl_forecasting.pkl', 'rb') as f:
    model = pickle.load(f)

# Title of the web app
st.title("IPL Player Prediction: Hardik Pandya's Runs Forecast")

# Input for the season (Year)
season = st.number_input("Enter the Season (Year):", min_value=2008, max_value=2028, value=2023)

# Convert the input season to a Timestamp (e.g., Jan 1st of that year)
season_timestamp = pd.Timestamp(f'{season}-01-01')

# Button to make prediction
if st.button("Predict Runs"):
    # Prepare the input data for prediction
    # The model expects a time series with proper formatting, so create an appropriate DataFrame
    input_data = pd.DataFrame({'season': [season_timestamp]})
    input_data.set_index('season', inplace=True)

    # Predict the runs using the SARIMAX model (assuming the model is trained on seasonal data)
    try:
        # Since the model is likely trained on previous seasons, use the predict method with the proper arguments
        prediction = model.predict(start=input_data.index[0], end=input_data.index[0])  # Predict for the input season
        st.write(f"Predicted Runs for Season {season}: {prediction[0]}")
    except Exception as e:
        st.error(f"Error in prediction: {e}")

# Option to download the pickle file (model)
st.download_button(
    label="Download the Model",
    data=open('ipl_forecasting.pkl', 'rb').read(),
    file_name='ipl_forecasting.pkl',
    mime='application/octet-stream'
)


