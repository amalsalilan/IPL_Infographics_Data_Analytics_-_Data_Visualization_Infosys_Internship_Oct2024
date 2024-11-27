import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Import NumPy explicitly

# Title and description
st.title("CSK Match Points Forecast (Pre-forecasted Data)")
st.write("This app displays the forecasted match points for Chennai Super Kings (CSK) using pre-generated values.")

# File uploader for the forecasted match points dataset
uploaded_file = st.file_uploader("Upload your forecasted dataset (CSV format)", type=["csv"])
if uploaded_file:
    # Load data
    forecast_data = pd.read_csv(uploaded_file)
    st.write("Forecasted Data Preview:")
    st.dataframe(forecast_data)

    # Input fields for forecast customization
    st.sidebar.header("Forecast Settings")

    # Number of forecast steps
    num_steps = st.sidebar.number_input("Number of forecast steps:", min_value=1, max_value=10, value=5)

    # Start season for forecast
    start_season = forecast_data['season'].max()
    end_season = start_season + num_steps  # Calculate the end season based on input
    st.sidebar.write(f"Forecasting until season {end_season}")

    # Generate the forecasted seasons based on the input
    forecast_seasons = list(range(start_season + 1, end_season + 1))

    # Visualization of forecasted data
    st.write("Visualization:")
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot historical data
    ax.plot(forecast_data['season'], forecast_data['forecasted_matchpoints'], marker='o', linestyle='-', color='red', label='Forecasted Match Points')

    # Simulating the forecast for the user-defined steps (example, using existing forecast values)
    forecasted_values = forecast_data['forecasted_matchpoints'].iloc[-1] + (0.5 * np.arange(1, num_steps + 1))  # Mock forecast (adjust as needed)

    # Plot the forecasted data
    ax.plot(forecast_seasons, forecasted_values, marker='o', linestyle='--', color='blue', label='Projected Match Points')

    ax.set_title(f"CSK Forecasted Match Points (until {end_season})")
    ax.set_xlabel("Season")
    ax.set_ylabel("Match Points")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
