import streamlit as st
import pickle
import pandas as pd
teams = ['Chennai Super Kings','Delhi Capitals,Punjab Kings',
'Kolkata Knight Riders','Mumbai Indians',
'Rajasthan Royals',
'Royal Challengers Bangalore',
'Sunrisers Hyderabad',
'Gujarat Titans',
'Lucknow Super Giants']
cities = ['Ahmedabad', 'Bengaluru','Chennai','Delhi',
          'Dharamsala','Hyderabad','Indore','Jaipur',
          'Kolkata','Mohali','Mumbai','Nagpur','Pune',
          'Rajkot','Ranchi','Raipur','Visakhapatnam','Kanpur']
pipe= pickle.load(open('pipe.pkl','rb'))

st.title('IPL Win predictor')

col1, col2 =  st.columns(2)
with col1:
    batting_team = st.selectbox('select the batting team' ,sorted(teams))
with col2:
    bowling_team = st.selectbox('select the bowling team' , sorted(teams))
selected_city = st.selectbox('select host city',sorted(cities))
col3,col4,col5,col6 = st.columns(4)
with col3:
    score = st.number_input('score')    
with col4:
    overs = st.number_input('overs completed')
with col5:
    wickets=st.number_input('Wickets out')
with col6:
    target=st.number_input('Target')
if st.button('predict probability'):
    runs_left= target - score
    balls_left = 120 -(overs*6)
    wickets = 10 - wickets
    crr= score/overs
    rrr = (runs_left*6)/balls_left
    
    input_df= pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],
                            'city':[selected_city],'runs_left':[runs_left],
                            'balls_left':balls_left,'Wickets':[wickets],'total_runs':[target],
                            'crr':[crr],'rrr':[rrr]})
    result = pipe.predict_proba(input_df)
    loss= result[0][0]
    Win = result[0][1]
    st.text(batting_team + " - " + str(round(Win*100)) + "%")    
    st.text(bowling_team + " - " + str(round(loss*100)) + "%") 