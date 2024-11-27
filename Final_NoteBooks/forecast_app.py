import io
import base64
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

# Ensure Matplotlib compatibility with Streamlit
plt.switch_backend("agg")

# Load dataset and validate structure
try:
    df = pd.read_csv('points_table.csv')
    # Ensure required columns are present
    required_columns = ["season", "rank", "name"]
    if not all(col in df.columns for col in required_columns):
        st.error(f"Dataset must contain the following columns: {required_columns}")
        st.stop()
except FileNotFoundError:
    st.error("The file 'points_table.csv' was not found. Please ensure it is in the correct directory.")
    st.stop()

# Streamlit Application
def main():
    st.set_page_config(page_title="Team Ranking Forecast", layout="wide")  # Wide layout for better UI

    # Custom CSS to adjust background color and add transparent white for cells
    st.markdown(
        """
        <style>
        /* Set app background to black */
        body {
            background-color: black;
            color: white;
        }

        /* Adjust the width of the sidebar */
        .css-1d391kg {width: 200px;}  /* Adjust the width of the sidebar */

        /* Center align tables and plots */
        .center-table {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Cell styling with fixed height and transparent white background */
        .cell {
            background-color: rgba(255, 255, 255, 0.1); /* Transparent white background with 50% opacity */
            border-radius: 15px; /* Rounded corners */
            padding: 10px;
            margin: 10px;
            height: 750px; /* Set a fixed height */
            overflow: auto; /* Enable scrolling if content overflows */
        }

        .table-container {
            margin: 20px;
            border-radius: 15px; /* Rounded corners */
            background-color: rgba(0, 0, 0,.1); /* Transparent white background with 50% opacity */
            padding: 20px;
            margin: 10px;
            height: 650px; /* Set a fixed height for the table */
            overflow-y: auto; /* Enable scrolling for the table */
        }

        .plot-container {
            background-color: rgba(255, 255, 255, 0.1); /* Transparent white background with 50% opacity */
            padding: 20px;
            border-radius: 15px;
            margin: 10px;
            height: 300px; /* Set a fixed height for the plot */
            overflow: hidden;
        }

        </style>
        """, unsafe_allow_html=True
    )

    # Header with a centered title and custom styling
    st.markdown(
        "<h1 style='text-align: center; color: #4CAF50;'>Team Ranking Forecasting App</h1>",
        unsafe_allow_html=True,
    )

    # Sidebar for Inputs (minimized to take up less space)
    with st.sidebar:
        st.header("Configuration Panel")
        st.write("Use the options below to customize your forecast.")

        # Sidebar for Team Selection
        team_names = df["name"].unique()
        selected_team = st.selectbox(
            "Select a Team:",
            team_names,
            help="Choose the team you want to analyze.",
        )

        # Forecast steps slider - Change to 10 seasons
        forecast_steps = st.slider(
            "Number of Seasons to Forecast:",
            1,
            10,  # Changed max value to 10
            10,  # Default forecast steps set to 10
            help="Select how many seasons into the future you want predictions for.",
        )

    # Display selected team information with markdown for styling
    st.markdown(
        f"<h3 style='text-align: center;'>Selected Team: {selected_team}</h3>",
        unsafe_allow_html=True,
    )

    # Filter the data for the selected team
    team_data = df[df["name"] == selected_team][["season", "rank"]].set_index("season")

    # Validate team data
    if team_data.empty:
        st.warning(f"No data available for the selected team: {selected_team}")
        return

    # Ensure a continuous time series by reindexing
    team_data = team_data.sort_index()

    # 2x2 Layout with full width and custom margins for a cleaner look
    col1, col2 = st.columns(2)

    # **Table inside the .cell container** 
    with col1:
        # Display historical data as a table
        st.markdown(
            "<div class='cell'>"
            "<h4 style='text-align: center;'>Historical Data</h4>"
            f"<div class='table-container'>{team_data.to_html(classes='table', index=True)}</div>"
            "</div>",
            unsafe_allow_html=True
        )

    # Historical Ranking plot
    fig, ax = plt.subplots(figsize=(12, 8))  # Increased size for larger plot
    ax.plot(team_data.index, team_data["rank"], marker="o", label="Historical Rank")
    ax.invert_yaxis()  # Lower rank is better
    ax.set_title(f"Ranking of {selected_team} Over Seasons")
    ax.set_xlabel("Season")
    ax.set_ylabel("Rank")
    ax.legend()

    # Save plot to a variable (as a byte stream)
    img_stream = io.BytesIO()  # Create a byte stream to save the image
    fig.savefig(img_stream, format='png')  # Save the figure as PNG to the byte stream
    img_stream.seek(0)  # Go to the beginning of the byte stream

    # Convert the image byte stream to base64
    img_base64 = base64.b64encode(img_stream.getvalue()).decode('utf-8')

    # Embed the image in markdown using base64
    img_html = f'<img src="data:image/png;base64,{img_base64}" alt="Historical Ranking" style="width:100%; height:auto; border-radius:15px;">'

    with col2:
        st.markdown(
            "<div class='cell'>"
            "<h4 style='text-align: center;'>Historical Ranking</h4>"
            f"{img_html}"  # Insert the base64 image here
            "</div>", unsafe_allow_html=True
        )

    # Stationarity Test
    def test_stationarity(series):
        if series.nunique() == 1:
            return None  # Series is constant
        adf_result = adfuller(series)
        return adf_result[1]  # p-value

    p_value = test_stationarity(team_data["rank"])
    if p_value is None:
        st.warning(
            "The time series is constant. Forecasting cannot proceed for this dataset."
        )
        return
    elif p_value > 0.05:
        st.warning("The time series is non-stationary. Differencing will be applied.")

    # Differencing if necessary
    team_data_diff = team_data["rank"].diff().dropna()

    # Fit ARIMA Model
    model = ARIMA(team_data["rank"], order=(1, 1, 0))  # (p, d, q)
    arima_model = model.fit()

    # Forecast Future Ranks
    forecast = arima_model.get_forecast(steps=forecast_steps)
    forecast_index = range(team_data.index[-1] + 1, team_data.index[-1] + 1 + forecast_steps)
    forecast_rank = forecast.predicted_mean

    # Display Forecasted Data in the third cell
    with col1:
        st.markdown(
            "<div class='cell'>"
            "<h4 style='text-align: center;'>Forecasted Ranks</h4>"
            f"{pd.DataFrame({'Season': forecast_index, 'Forecasted Rank': forecast_rank}).to_html(classes='table-container', index=False)}"
            "</div>",
            unsafe_allow_html=True
        )

    # Forecast Plot
    fig, ax = plt.subplots(figsize=(12, 8))  # Increased size for larger plot
    ax.plot(team_data.index, team_data["rank"], marker="o", label="Historical Data")
    ax.plot(forecast_index, forecast_rank, marker="x", label="Forecasted Data", color="red")
    ax.invert_yaxis()
    ax.set_title(f"Ranking Forecast for {selected_team}")
    ax.set_xlabel("Season")
    ax.set_ylabel("Rank")
    ax.legend()

    # Save plot to a variable (as a byte stream)
    img_stream = io.BytesIO()  # Create a byte stream to save the image
    fig.savefig(img_stream, format='png')  # Save the figure as PNG to the byte stream
    img_stream.seek(0)  # Go to the beginning of the byte stream

    # Convert the image byte stream to base64
    img_base64 = base64.b64encode(img_stream.getvalue()).decode('utf-8')

    # Embed the image in markdown using base64
    img_html = f'<img src="data:image/png;base64,{img_base64}" alt="Forecast Plot" style="width:100%; height:auto; border-radius:15px;">'

    # Plot Forecast in the fourth cell
    with col2:
        st.markdown(
            "<div class='cell'>"
            "<h4 style='text-align: center;'>Forecast Plot</h4>"
            f"{img_html}"  # Insert the base64 image here
            "</div>", unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
