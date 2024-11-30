import streamlit as st
import subprocess
from PIL import Image
import pandas as pd
import util._forecasting as _forecasting

# Streamlit app configuration
st.set_page_config(
    page_title="IPL Team Points Forecasting",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Title and description
st.title("🏏 IPL Team Points Forecasting App")
st.write(
    """
    Predict how your favorite IPL team will perform in the upcoming seasons!  
    Select a team, choose the number of future seasons to forecast, and view the results in an easy-to-read chart.
    """
)

# Dataset path
DATASET_PATH = "util/processed_points.csv"

# Team selection dropdown
teams = [
    "Gujarat Titans", "Chennai Super Kings", "Lucknow Super Giants",
    "Mumbai Indians", "Rajasthan Royals",
    "Royal Challengers Bangalore", "Kolkata Knight Riders",
    "Kings XI Punjab", "Delhi Capitals", "Sunrisers Hyderabad"
]

st.sidebar.header("Forecast Parameters")
team_name = st.sidebar.selectbox(
    "Select a Team:",
    options=teams,
    help="Choose the IPL team for which you want to forecast points."
)

# Number of seasons input
steps = st.sidebar.number_input(
    "Forecast Seasons:",
    min_value=3,
    max_value=10,
    value=5,
    step=1,
    help="Enter the number of future seasons to forecast (between 3 and 10)."
)

# Action button
if st.sidebar.button("🌟 Forecast"):
    if team_name and steps > 0:
        try:
            # Call the forecasting function
            forecast_results, plot_path = _forecasting.forecast_points(team_name, DATASET_PATH, steps)

            if isinstance(forecast_results, dict):
                # Display forecast results
                st.subheader(f"📊 Forecast Results for {team_name}")
                st.dataframe(pd.DataFrame(forecast_results, index=[0]).T, use_container_width=True)

                # Display forecast plot
                if plot_path:
                    img = Image.open(plot_path)
                    st.image(
                        img,
                        caption=f"Forecast Plot for {team_name}",
                        use_column_width=True,
                    )
            else:
                st.error(f"An error occurred during forecasting: {forecast_results}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
    else:
        st.error("Please select a team and enter a valid number of forecast seasons.")

# Footer
st.write("---")
st.write(
    "Developed with ❤️ for IPL enthusiasts. Have fun forecasting!"
)
