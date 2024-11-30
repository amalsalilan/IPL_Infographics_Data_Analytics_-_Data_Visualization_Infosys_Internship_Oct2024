import streamlit as st

# Configure the app
st.set_page_config(
    page_title="IPL Analytics Hub",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for background image
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("util/image.png");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# App title
st.title("🏏 Welcome to the IPL Analytics Hub!")
st.write(
    """
    Dive into the world of IPL analytics!  
    Use the sidebar to explore various features like team performance forecasting, match score predictions, and much more.
    """
)

# Sidebar content
st.sidebar.header("Available Features")

# Hardcoded list of apps with descriptions
apps = {
    "Forecasting App": {
        "description": "Predict how your favorite IPL team will perform in the upcoming seasons. View future team points trends using historical data.",
        "icon": "🌟"
    },
    "Score Prediction App": {
        "description": "Predict cumulative runs in an ongoing IPL match based on current match features such as overs, wickets, and run rate.",
        "icon": "📊"
    },
    "Winner Prediction App": {
        "description": "Calculate the winning probability of an IPL match based on match stats, including runs scored, wickets lost, and target runs.",
        "icon": "📈"
    }
}

# Display available apps in the sidebar
st.sidebar.write("Select a feature to explore:")
for app_name, details in apps.items():
    st.sidebar.write(f"- {details['icon']} **{app_name}**")

# Main content for About This Platform
st.write("---")
st.subheader("About This Platform")
st.write(
    """
    This platform offers various tools and insights into IPL data. Below are the details of each feature available:
    """
)
for app_name, details in apps.items():
    st.write(f"### {details['icon']} {app_name}")
    st.write(f"- {details['description']}")

# Example dynamic content
st.write("---")
st.info("Navigate to various features using the sidebar to gain insights into IPL data.")

# Footer
st.write("---")
st.write("Developed with ❤️ by Data Enthusiasts.")
