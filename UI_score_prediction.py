import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained Ridge model
try:
    with open('/content/sample_data/predicted_runs.pkl', 'rb') as file:
        model = pickle.load(file)
    st.success("Model loaded successfully!")
except FileNotFoundError:
    st.error("Error: Model file not found. Ensure 'predicted_runs.pkl' is available.")
    st.stop()

# Mock data used during training for encoding
home_teams = ['CSK', 'GT', 'PBKS', 'KKR', 'LSG', 'DC', 'RR', 'SRH', 'MI', 'RCB', 'RPS', 'GL', 'PWI', 'Kochi' ]
away_teams = ['CSK', 'GT', 'PBKS', 'KKR', 'LSG', 'DC', 'RR', 'SRH', 'MI', 'RCB', 'RPS', 'GL', 'PWI', 'Kochi' ]
innings = ['1st Innings', '2nd Innings']

# Function to preprocess input data
def preprocess_input(season, match_id, home_team, away_team, current_innings, over, ball, batsman1_runs, batsman1_balls):
    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'season': [season],
        'match_id': [match_id],
        'home_team': [home_team],
        'away_team': [away_team],
        'current_innings': [current_innings],
        'over': [over],
        'ball': [ball],
        'batsman1_runs': [batsman1_runs],
        'batsman1_balls': [batsman1_balls]
    })
    
    # One-hot encode categorical columns
    input_data_encoded = pd.get_dummies(input_data, columns=['home_team', 'away_team', 'current_innings'])
    
    # Ensure consistent feature ordering
    expected_columns = model.feature_names_in_  # Columns used during training
    for col in expected_columns:
        if col not in input_data_encoded:
            input_data_encoded[col] = 0  # Add missing columns with zero values

    input_data_encoded = input_data_encoded[expected_columns]  # Reorder columns
    return input_data_encoded.values

# Title of the web app
st.title("IPL Match Winner Prediction")
st.write("Predict the winner of an IPL match based on match details.")

# Input fields for the user
season = st.number_input("Season (e.g., 2023):", min_value=2008, max_value=2028, value=2023, step=1)
match_id = st.number_input("Match ID (e.g., 101):", min_value=1, value=1, step=1)
home_team = st.selectbox("Home Team:", home_teams)
away_team = st.selectbox("Away Team:", away_teams)
current_innings = st.selectbox("Current Innings:", innings)
over = st.number_input("Over (0-20):", min_value=0, max_value=20, step=1)
ball = st.number_input("Ball (0-6):", min_value=0, max_value=6, step=1)
batsman1_runs = st.number_input("Batsman 1 Runs:", min_value=0, step=1)
batsman1_balls = st.number_input("Batsman 1 Balls:", min_value=0, step=1)

# Prediction button
if st.button("Predict Winner"):
    # Map innings input to numerical encoding
    current_innings_encoded = 1 if current_innings == "1st Innings" else 2
    
    # Preprocess the input
    try:
        input_data = preprocess_input(
            season, match_id, home_team, away_team, current_innings_encoded, over, ball, batsman1_runs, batsman1_balls
        )
        
        # Make prediction
        prediction = model.predict(input_data)
        winner = "Home Team" if prediction[0] == 1 else "Away Team"
        st.success(f"The predicted winner is: {winner}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")

# Footer
st.write("Note: This prediction is based on a machine learning model and may not always be accurate.")
