# IPL Infographics: Data Analytics & Data Visualization

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](#)
[![Contributors](https://img.shields.io/badge/Contributors-9-orange.svg)](#contributors)

## Table of Contents

1. [Introduction](#introduction)
2. [Project Objectives](#project-objectives)
3. [Project Structure](#project-structure)
4. [Use Cases](#use-cases)
5. [Modules Implemented](#modules-implemented)
6. [Data Exploration and Preprocessing](#data-exploration-and-preprocessing)
7. [Modeling](#modeling)
8. [Results](#results)
9. [Visualizations](#visualizations)
10. [How to Use](#how-to-use)
11. [Branches and Contributions](#branches-and-contributions)
12. [Dependencies](#dependencies)
13. [Contributing](#contributing)
14. [Contributors](#contributors)
15. [Acknowledgements](#acknowledgements)
16. [License](#license)
17. [Contact Information](#contact-information)

---

## Introduction

**IPL Infographics: Data Analytics & Data Visualization**

![IPL Logo](images/ipl_logo.png)

The **Indian Premier League (IPL)** is a globally renowned Twenty20 cricket tournament held annually in India. This project involves performing comprehensive data analysis, predictive modeling, and creating insightful visualizations based on IPL data. Our aim is to uncover patterns, trends, and insights that can inform stakeholders and enthusiasts about various aspects of the tournament.

---

## Project Objectives

- **Data Analysis**: Gain insights into player performances, team trends, and venue statistics.
- **Predictive Modeling**: Build models to predict in-game scores, match winners, and forecast player performance.
- **Data Visualization**: Create interactive and informative visualizations to effectively communicate findings.
- **Collaboration**: Leverage the strengths of individual team members through branch-specific contributions.

---

## Project Structure

Due to the collaborative nature of this internship project, the repository is organized with multiple branches:

- **Main Branch**: Contains the consolidated project with all functionalities and final deliverables.
- **Intern Branches**: Individual contributions are available in sub-branches named after each intern.

---

## Use Cases

The project addresses three primary use cases:

1. **Predicting In-Game Score**
   - **Approach**: Regression analysis.
   - **Best Models**: Random Forest Regression and XGBoost Regression.

2. **Predicting the Winner**
   - **Approach**: Classification algorithms.
   - **Models Used**: Various machine learning classification models (e.g., Logistic Regression, Decision Trees).

3. **Forecasting Player Performance**
   - **Approach**: Time series forecasting.
   - **Model Used**: ARIMA model (suitable for datasets with fewer data points).

---

## Modules Implemented

The project is divided into the following modules:

1. **Data Collection (DC)**
2. **Data Exploration and Preprocessing (DEP)**
3. **Model Building (MB)**
4. **Model Evaluation & Presentation (MEP)**

---

## Data Exploration and Preprocessing

### Initial Exploration

- Utilized **Python**, **NumPy**, and **Pandas** for statistical analysis and data manipulation.
- Conducted initial data exploration to understand data distribution and variables.

### Exploratory Data Analysis (EDA)

- Employed **Matplotlib**, **Seaborn**, and **Plotly** for data visualization.
- Created comprehensive visualizations to identify hidden patterns and insights.

#### Sample Visualizations

![Top 10 Scoring Batsmen](images/top_10_batsmen.png)
*Figure 1: Top 10 Scoring Batsmen in the IPL.*

![Matches Played in Top Cities](images/top_cities_matches.png)
*Figure 2: Number of IPL Matches Played in Top 20 Cities.*

### Data Preprocessing

- **Handling Missing Values**: Applied techniques like mean/median imputation and interpolation.
- **Data Inconsistencies**: Resolved inconsistencies and ensured data quality.
- **Encoding**: Performed nominal and ordinal encoding for categorical variables.
- **Outlier Detection**: Used Z-scores and IQR methods to identify and treat outliers.
- **Trend Analysis**: Analyzed trends, seasonality, and randomness in the data.

---

## Modeling

### Baseline Models

- Established baseline models to serve as a benchmark.

### Advanced Models

- **Regression Models**: Random Forest and XGBoost provided superior performance for in-game score prediction.
- **Classification Models**: Implemented various algorithms to predict match winners.
- **Time Series Models**: Used ARIMA for forecasting player performance due to its effectiveness with limited data points.

### Model Optimization

- **Hyperparameter Tuning**: Utilized randomized grid search to optimize model parameters.
- **Cross-Validation**: Applied cross-validation to check for overfitting and ensure model generalizability.

### Inferencing and UI

- Saved encoded and pretrained models.
- Developed inferencing scripts for making predictions on new data.
- Created a user interface for model interaction.

---

## Results

Our advanced modeling approaches significantly outperformed the baseline models:

- **In-Game Score Prediction**: Achieved high accuracy with Random Forest and XGBoost regression models.
- **Winner Prediction**: Successfully predicted match outcomes using classification algorithms.
- **Player Performance Forecasting**: Effectively forecasted performance metrics using the ARIMA model.

---

## Visualizations

### Team-wise Analysis

![Win/Loss Analysis](images/team_win_loss.png)
*Figure 3: Team Win/Loss Analysis by Runs and Wickets.*

### Venue-wise Analysis

![Venue Performance](images/venue_performance.png)
*Figure 4: Team Winning Performance at Different Venues.*

### Toss Decisions Impact

![Toss Decision Heatmap](images/toss_decision_heatmap.png)
*Figure 5: Heatmap of Toss Decisions and Their Impact on Match Outcomes.*

### Player Performance Forecasting

![Player Performance Forecast](images/player_performance_forecast.png)
*Figure 6: Forecasted Performance Metrics for a Selected Player Using ARIMA Model.*

### Feature Importance

![Feature Importance](images/feature_importance.png)
*Figure 7: Feature Importance Derived from the XGBoost Model.*

### Model Performance Comparison

![Model Comparison](images/model_performance_comparison.png)
*Figure 8: Comparison of Model Performance Metrics Across Different Algorithms.*

---

## How to Use

### Clone the Repository

```bash
git clone https://github.com/your-repo/ipl-infographics.git
```

### Install Dependencies

Ensure you have **Python 3.x** installed. Install required packages:

```bash
pip install -r requirements.txt
```

### Running the Models

Navigate to the respective directories for each use case and run the scripts as instructed:

- **In-Game Score Prediction**:

  ```bash
  python models/regression/in_game_score_prediction.py
  ```

- **Winner Prediction**:

  ```bash
  python models/classification/winner_prediction.py
  ```

- **Player Performance Forecasting**:

  ```bash
  python models/forecasting/player_performance_forecasting.py
  ```

### User Interface

To interact with the models via the UI:

1. Navigate to the `ui` directory.

   ```bash
   cd ui
   ```

2. Install UI-specific dependencies:

   ```bash
   pip install -r ui_requirements.txt
   ```

3. Run the UI application:

   ```bash
   python app.py
   ```

4. Open your web browser and go to `http://localhost:5000`.

---

## Branches and Contributions

- **Main Branch**: Contains the final consolidated project.
- **Intern Branches**: Individual contributions can be found in branches named after each intern.

---

## Dependencies

- **Programming Language**: Python 3.x

### Key Libraries

- **Data Manipulation**: NumPy, Pandas
- **Data Visualization**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: Scikit-Learn, XGBoost
- **Time Series Analysis**: Statsmodels (for ARIMA)
- **Web Framework**: Flask (for UI)
- **Others**: See `requirements.txt` for the full list.

---

## Contributing

We welcome contributions from team members:

1. **Fork** the repository.
2. **Create** a feature branch:

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit** your changes:

   ```bash
   git commit -m 'Add a feature'
   ```

4. **Push** to the branch:

   ```bash
   git push origin feature/YourFeature
   ```

5. **Submit** a pull request for review.

---

## Contributors

- **Rahul Sharma** - *Data Collection and Preprocessing*
- **Ananya Gupta** - *Exploratory Data Analysis and Visualization*
- **Vikram Singh** - *Modeling and Evaluation*
- **Neha Patel** - *User Interface Development*
- **Amit Desai** - *Project Coordinator*

---

## Acknowledgements

We extend our gratitude to all interns and mentors who contributed to this project, making it a valuable learning experience.

- **Mentors**:
  - **Dr. Arjun Mehta** - Data Science Expert
  - **Ms. Kavita Rao** - Machine Learning Specialist

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact Information

For any queries or suggestions, please reach out to the project maintainers.

- **Project Lead**: Amit Desai
- **Email**: [projectlead@example.com](mailto:projectlead@example.com)

---

## Future Work

- **Expand Dataset**: Incorporate more seasons and detailed player statistics.
- **Advanced Modeling**: Explore deep learning models for prediction tasks.
- **Real-time Data**: Implement real-time data fetching and model updating.
- **Enhanced UI**: Develop a more interactive and user-friendly interface with dashboards.

---

## Notes

- All visualizations and images are stored in the `images` directory.
- For detailed analysis and reports, refer to the `reports` directory.
- The codebase follows PEP 8 style guidelines for Python code.

---

**Disclaimer**: This project is for educational purposes as part of an internship program. The data and analyses are based on available IPL datasets and are intended to demonstrate data analytics and visualization techniques.

---
