import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('ipl_pred_model_1.pkl', 'rb') as file:
    model = pickle.load(file)

# Title and description
st.title('IPL Match Winner Prediction')
st.write('Enter the details of the current match situation to predict the outcome.')

# Input fields
current_innings_encoded = st.selectbox('Current Innings (1 for 1st innings, 2 for 2nd innings):', [1, 2])
over = st.number_input('Over:', min_value=0, max_value=20, step=1)
ball = st.number_input('Ball:', min_value=0, max_value=6, step=1)
run_rate = st.number_input('Current Run Rate:', min_value=0.0, max_value=36.0, step=0.1)
wickets_lost = st.number_input('Wickets Lost:', min_value=0, max_value=10, step=1)

# Predict button
if st.button('Predict Winner'):
    # Prepare the input data
    input_data = np.array([[current_innings_encoded, over, ball, run_rate, wickets_lost]])

    # Get the prediction
    prediction = model.predict(input_data)

    # Display the result
    st.write(f'The predicted outcome is: {"Team 1 wins" if prediction[0] == 1 else "Team 2 wins"}')

# Footer
st.write('Note: This is a machine learning model prediction and may not always be accurate.')