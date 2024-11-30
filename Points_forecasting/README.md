# 🏏 IPL Team Points Forecasting

A web app to predict future IPL team points using ARIMA-based forecasting models. Explore historical trends and predict team performance in upcoming seasons! 🎉

## 📋 Project Overview

This tool allows cricket enthusiasts and analysts to forecast IPL team points for future seasons. Built with Streamlit, it features an intuitive UI and interactive data visualization.

## 🔍 Features

1. **Historical and Forecasted Trends:**
   - View past IPL team performance and future forecasts.

2. **Interactive Visualizations:**
   - Graphical insights using Plotly for historical and forecasted points.

3. **Custom Forecasting:**
   - Predict points for 3 to 10 future IPL seasons.

## 🗂️ Repository Structure

| File/Directory          | Description                                                 |
|-------------------------|-------------------------------------------------------------|
| `forecasting_app.py`    | Streamlit-based app for forecasting team points.            |
| `util/_forecasting.py`  | Core ARIMA-based forecasting logic.                         |
| `util/processed_points.csv` | Processed dataset with historical IPL match points.      |
| `requirements.txt`      | List of Python dependencies for the project.                |
| `README.md`             | Documentation and setup guide.                              |

## 🚀 Getting Started

### Prerequisites

- Python 13.0+
- Pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ipl-points-forecast.git
   cd ipl-points-forecast

2. Install dependencies:

```bash
pip install -r requirements.txt
```
Run the Application
Start the Streamlit app:

```
streamlit run forecasting_app.py
```
Open the app in your browser at http://localhost:8501.

## 🧠 How It Works

### Input:
- Choose an IPL team and forecast horizon (3–10 seasons) via the sidebar.

### Data Processing:
- Historical data is transformed to ensure stationarity using differencing.

### ARIMA Model:
1. Optimal `(p, d, q)` parameters are selected through grid search.
2. The model forecasts future points for selected seasons.

### Output:
- Visualize historical and forecasted team points using interactive charts.

---

## 📈 ARIMA Model Details

### Stationarity:
- Time series data is differenced to remove trends.

### Optimal Parameters:
- Parameters `(p, d, q)` are determined via grid search for the ARIMA model.

### Forecasting:
- Predicts future IPL team points for the selected forecast horizon.

---

## 📂 Dataset Details

### Source:
- `util/processed_points.csv`: Contains historical IPL team points data.

### Columns:
- `name`: Team name.
- `season`: IPL season year.
- `matchpoints`: Points earned in a season.

---

## 🤝 Contributing

- Fork the repository and create a pull request.
- Report bugs or request features by opening issues.

---

## 🛠️ Troubleshooting

### ARIMA Model Errors:
- Ensure sufficient historical data exists for the selected team.

### Streamlit App Issues:
- Verify Python version compatibility and installed dependencies.

---

# ❤️ Credits

Developed with ❤️ for IPL enthusiasts. Have fun forecasting! 🎉
