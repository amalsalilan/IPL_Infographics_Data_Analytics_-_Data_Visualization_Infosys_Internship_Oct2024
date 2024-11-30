import streamlit as st 
import pandas as pd
from forecast_script import forecast_points  # Import your forecasting function

st.title("Team Points Forecasting")

# Upload Dataset
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type="csv")
if uploaded_file:
    dataset_path = uploaded_file.name
    with open(dataset_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Input Form
    team_name = st.text_input("Enter Team Name:")
    steps = st.number_input("Enter Number of Seasons to Forecast:", min_value=1, step=1, value=3)

    if st.button("Forecast"):
        if team_name and dataset_path:
            results, plot_path = forecast_points(team_name, dataset_path, steps)

            if plot_path:
                st.write("### Forecast Results")
                for season, points in results.items():
                    st.write(f"{season}: {points} points")

                st.image(plot_path, caption="Forecast Plot")
                with open(plot_path, "rb") as img:
                    btn = st.download_button(label="Download Plot", data=img, file_name="forecast_plot.png")
            else:
                st.error(f"Error: {results}")
        else:
            st.error("Please provide valid inputs!")
