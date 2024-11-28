import streamlit as st
import pickle
import pandas as pd

# Load the saved XGBoost model
with open(r"C:\Users\Reshm\Documents\Infosys Intern\IPL_Infographics_Data_Analytics_-_Data_Visualization_Infosys_Internship_Oct2024\xgb_model.pkl", 'rb') as f:
    model = pickle.load(f)

# Load the LabelEncoder for team encoding
with open(r"C:\Users\Reshm\Documents\Infosys Intern\IPL_Infographics_Data_Analytics_-_Data_Visualization_Infosys_Internship_Oct2024\team_encoder.pkl", 'rb') as f:
    team_encoder = pickle.load(f)

# Apply custom CSS for better styling
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
            font-family: Arial, sans-serif;
        }
        .sidebar .sidebar-content {
            background-color: #0066cc;
            color: white;
        }
        .stButton button {
            background-color: #28a745;
            color: white;
            font-size: 16px;
        }
        .stSlider > div {
            color: #0066cc;
        }
    </style>
""", unsafe_allow_html=True)

# App title and description
st.title("📊 IPL Run Prediction App")
st.subheader("🏏 Predict the cumulative runs of an ongoing match based on the match's features.")

# Sidebar for user input
st.sidebar.header("🎯 Input Match Features")
st.sidebar.markdown("Provide the details of the match to predict the cumulative runs:")

# Dropdowns for team selection
teams = list(team_encoder.classes_)
home_team = st.sidebar.selectbox("🏠 Select Home Team", teams)
away_team = st.sidebar.selectbox("🚩 Select Away Team", teams)
current_innings = st.sidebar.selectbox("⚾ Current Batting Team", teams)

# Sliders and input for match data
over = st.sidebar.slider("Over", 0, 20, 10)
ball = st.sidebar.slider("Ball", 0, 6, 3)
run_rate = st.sidebar.number_input("📈 Current Run Rate", min_value=0.0, max_value=20.0, value=6.0, step=0.1)
wickets_lost = st.sidebar.slider("⚡ Wickets Lost", 0, 10, 2)

# Prediction logic
if st.sidebar.button("🔍 Predict"):
    # Encode team inputs
    home_team_encoded = team_encoder.transform([home_team])[0]
    away_team_encoded = team_encoder.transform([away_team])[0]
    current_innings_encoded = team_encoder.transform([current_innings])[0]
    
    # Create input DataFrame
    input_data = pd.DataFrame({
        'over': [over],
        'ball': [ball],
        'run_rate': [run_rate],
        'wickets_lost': [wickets_lost],
        'home_team_encoded': [home_team_encoded],
        'away_team_encoded': [away_team_encoded],
        'current_innings_encoded': [current_innings_encoded]
    })
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display prediction
    st.subheader("📊 Prediction Result")
    st.success(f"🏏 **Predicted Cumulative Runs:** {prediction[0]:.2f}")
    st.markdown(
        "The predicted cumulative runs are based on the current match scenario. Use this prediction for strategic decision-making!"
    )
