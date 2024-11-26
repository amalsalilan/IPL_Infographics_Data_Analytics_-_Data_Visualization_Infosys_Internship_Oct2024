import streamlit as st
import pickle
import numpy as np
import pandas as pd
def main():
    st.title('IPl Score Regressor')

    with open("ipl_reg_model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    with open("encoder.pkl", "rb") as model_file1:
        encoder = pickle.load(model_file1)
    

    # Title and description
    st.title("Probable cumulative scorce predictor")
    st.write("This app predicts the cummulative score")

    # Dropdown options for categorical fields
    teams = ['MI', 'KKR', 'SRH', 'DC', 'CSK', 'KXIP', 'RR', 'LSG', 'RCB', 'GT']  # Example team names
    overs=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    balls=[1,2,3,4,5,6]

    # Dropdown fields for teams and venues
    Current_over=st.selectbox("over",overs)
    Current_Ball=st.selectbox("Ball",balls)
    Home_team = st.selectbox("Batting Team", teams)
    Away_team = st.selectbox("Bowling Team", teams)
    Season=st.number_input("season no",min_value=0, max_value=500, value=0)
    Matchid=st.number_input("Match id",min_value=0, max_value=10000000000, value=0)
    Current_innings=st.selectbox("Current Innings",teams)
    Wickets_down = st.number_input("Wickets Down", min_value=0, max_value=10, value=0)
    Run_rate=st.number_input("Current run rate",min_value=0, max_value=500, value=0)
   #

    

    input_data = {
        'over': [Current_over],
        'ball': [Current_Ball],
        'run_rate': [Run_rate],
        'wickets_lost': [Wickets_down],
        'season': [Season],
        'match_id':[Matchid],
        'home_team': [Home_team],
        'away_team': [Away_team],
        'current_innings': [Current_innings]
        
    }
    
    input_df = pd.DataFrame(input_data)
    categorical_features = input_df[['home_team', 'away_team', 'current_innings']]
    encoded_categorical = encoder.transform(categorical_features)
    non_categorical = input_df[['over', 'ball', 'run_rate', 'wickets_lost', 'season', 'match_id']]
    final_input = np.hstack([non_categorical, encoded_categorical])

    if(st.button("Predict")):

        predicted_outcome = model.predict(final_input)
    
        st.success(f'Cummulative runs :{predicted_outcome}')
if __name__ == '__main__':
  main()