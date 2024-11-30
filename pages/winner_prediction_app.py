import streamlit as st
import pickle
import numpy as np
import pandas as pd

def main():
    # Set page configuration
    st.set_page_config(page_title="IPL Winning Prediction", page_icon="📈", layout="wide")

    # Sidebar Header
    st.sidebar.header("Cricket Match Prediction")
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/4/41/IPL_2022_Logo.png", use_column_width=True)  # Replace with a relevant IPL image URL

    # Main Title and Description
    st.title("🏏 IPL Winning Prediction App")
    st.markdown("""
    This app predicts the **winning probability** of an IPL match based on the match stats.  
    Enter the details below to get the predictions!
    """)

    # Load the prediction model
    with open("util/ipl_pred_model.pkl", "rb") as model_file:
        model = pickle.load(model_file)

    # Define teams and venues
    teams = ['MI', 'KKR', 'SRH', 'DC', 'CSK', 'KXIP', 'RR', 'LSG', 'RCB', 'GT']  # Example team names
    venues = ['Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh',
              'M.Chinnaswamy Stadium, Bengaluru',
              'Himachal Pradesh Cricket Association Stadium, Dharamsala',
              'Arun Jaitley Stadium, Delhi',
              'Maharashtra Cricket Association Stadium, Pune',
              'Dr DY Patil Sports Academy, Mumbai', 'Eden Gardens, Kolkata',
              'Wankhede Stadium, Mumbai', 'Barabati Stadium, Cuttack',
              'Holkar Cricket Stadium, Indore', 'Sharjah Cricket Stadium',
              'Sawai Mansingh Stadium, Jaipur',
              'Sardar Patel (Gujarat) Stadium, Motera, Ahmedabad',
              'MA Chidambaram Stadium, Chepauk, Chennai',
              'Vidarbha Cricket Association Stadium, Jamtha, Nagpur',
              'Sheikh Zayed Stadium, Abu Dhabi',
              'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
              'SuperSport Park, Centurion',
              'Dubai International Cricket Stadium',
              'Narendra Modi Stadium, Motera, Ahmedabad',
              'Dr DY Patil Sports Academy, Navi Mumbai', 'Newlands, Cape Town',
              'Rajiv Gandhi International Stadium, Uppal, Hyderabad',
              'JSCA International Stadium Complex, Ranchi',
              'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam',
              "St George's Park, Port Elizabeth", 'Brabourne Stadium, Mumbai',
              'Kingsmead, Durban',
              'Shaheed Veer Narayan Singh International Stadium, Raipur',
              'Mangaung Oval, Bloemfontein',
              'The Wanderers Stadium, Johannesburg', 'Buffalo Park, East London',
              'Diamond Oval, Kimberley', 'Barsapara Cricket Stadium, Guwahati']

    # Collect user inputs
    st.sidebar.subheader("Match Details")
    batting_team = st.sidebar.selectbox("Batting Team", teams)
    bowling_team = st.sidebar.selectbox("Bowling Team", teams)
    toss_winner = st.sidebar.selectbox("Toss Winner", teams)
    venue = st.sidebar.selectbox("Venue", venues)

    runs_scored = st.number_input("🏏 Runs Scored", min_value=0, max_value=500, value=0, step=1)
    wickets_down = st.number_input("⚾ Wickets Down", min_value=0, max_value=10, value=0, step=1)
    current_over = st.number_input("Over (Completed)", min_value=0, max_value=20, value=0, step=1)
    current_ball = st.number_input("Balls in Current Over", min_value=0, max_value=6, value=0, step=1)
    target_runs = st.number_input("🎯 Target Runs", min_value=0, max_value=500, value=0, step=1)

    # Calculate derived inputs
    runs_left = target_runs - runs_scored
    balls_left = 20 * 6 - (current_over * 6 + current_ball)
    wickets_remaining = 10 - wickets_down
    crr = round((runs_scored * 6) / (current_over * 6 + current_ball), 2) if (current_over * 6 + current_ball) != 0 else 0
    rrr = round((runs_left * 6) / balls_left, 2) if balls_left > 0 else 0

    # Prepare input DataFrame
    input_data = pd.DataFrame({
        'BattingTeam': [batting_team],
        'BowlingTeam': [bowling_team],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets_remaining': [wickets_remaining],
        'target_runs': [target_runs],
        'crr': [crr],
        'rrr': [rrr],
        'toss_winner': [toss_winner],
        'venue': [venue]
    })

    # Prediction and visualization
    if st.button("💡 Predict Winning Probability"):
        predicted_outcome = model.predict(input_data)[0]
        win_probability = model.predict_proba(input_data)[0][1] * 100

        # Display probabilities
        st.subheader("🏆 Prediction Results")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label=f"{batting_team} Winning Probability", value=f"{round(win_probability, 2)}%")
        with col2:
            st.metric(label=f"{bowling_team} Winning Probability", value=f"{round(100 - win_probability, 2)}%")

        # Progress Bar
        st.progress(int(win_probability))

        # Highlight the predicted winner
        if predicted_outcome == 0:
            predicted_outcome = bowling_team
        else:
            predicted_outcome = batting_team
        st.success(f"The most probable winner is: **{predicted_outcome}**")


if __name__ == '__main__':
    main()
