import streamlit as st
import pandas as pd
from PIL import Image
import plotly.graph_objects as go
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
    Select a team, choose the number of future seasons to forecast, and view the results in an interactive chart.
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
            forecast_results, future_seasons, historical_data = _forecasting.forecast_points(team_name, DATASET_PATH, steps)

            if isinstance(forecast_results, dict): 
                # Display forecast results
                st.subheader(f"📊 Forecast Results for {team_name}")
                forecast_df = pd.DataFrame(list(forecast_results.items()), columns=["Season", "Predicted Points"])
                st.dataframe(forecast_df, use_container_width=True)

                # Plot forecast results interactively using Plotly
                st.subheader(f"📈 Forecasting Plot for {team_name}")

                fig = go.Figure()

                # Add historical data
                fig.add_trace(go.Scatter(
                    x=historical_data["Season"],
                    y=historical_data["Match Points"],
                    mode='lines+markers',
                    name='Historical Data',
                    line=dict(color='blue'),
                    marker=dict(size=8)
                ))

                # Add forecasted data
                fig.add_trace(go.Scatter(
                    x=future_seasons,
                    y=list(forecast_results.values()),
                    mode='lines+markers',
                    name='Forecasted Data',
                    line=dict(dash='dash', color='green'),
                    marker=dict(size=8)
                ))

                # Customize layout
                fig.update_layout(
                    title=f"{team_name} Points Forecast",
                    xaxis_title="Season",
                    yaxis_title="Match Points",
                    legend_title="Data Type",
                    template="plotly_white",
                    hovermode="x unified"
                )

                st.plotly_chart(fig, use_container_width=True)
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
