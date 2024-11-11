import streamlit as st
import pickle
import numpy as np
import pandas as pd
def main():
    st.title('IPl Prediction App')

    with open("ipl_pred_model_1.pkl", "rb") as model_file:
        model = pickle.load(model_file)

    # Title and description
    st.title("Cricket Match Outcome Prediction App")
    st.write("This app predicts the probability of winning based on match stats and teams.")

    # Dropdown options for categorical fields
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
       'Diamond Oval, Kimberley', 'Barsapara Cricket Stadium, Guwahati'] # Example venue names

    # Dropdown fields for teams and venues
    batting_team = st.selectbox("Batting Team", teams)
    bowling_team = st.selectbox("Bowling Team", teams)
    toss_winner = st.selectbox("Toss Winner", teams)
    venue = st.selectbox("Venue", venues)

    runs_scored = st.number_input("Runs Scored", min_value=0, max_value=500, value=0)
    wickets_down = st.number_input("Wickets Down", min_value=0, max_value=10, value=0)
    current_over = st.number_input("Current over",min_value=0,max_value=20)
    current_ball = st.number_input("Current ball",min_value=0,max_value=6)
    target_runs = st.number_input("Target Runs", min_value=0, max_value=500, value=0)   #

    runs_left = target_runs - runs_scored  #
    balls_left = 20*6 - (current_over*6+current_ball)   #
    wickets_remaining = 10 - wickets_down    #
    crr = round((runs_scored * 6) / (current_over * 6 + current_ball), 2) if (current_over * 6 + current_ball) != 0 else 0
    rrr = round((runs_left * 6) / balls_left, 2) if balls_left != 0 else 0           #

    input_data = {
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
    }
    
    input_df = pd.DataFrame(input_data)

    if(st.button("Predict")):

        predicted_outcome = model.predict(input_df)
        win_probability = model.predict_proba(input_df)[0][1] * 100
        st.success(f'Winning Probability of {batting_team} is : {round(win_probability, 2)}%')
        st.success(f'Winning Probability of {bowling_team} is : {round(100 - win_probability, 2)}%')
if __name__ == '__main__':
  main()