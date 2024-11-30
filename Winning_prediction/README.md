
# 🏏**IPL Winning Team Prediction**

A machine learning-powered web app that predicts IPL match winners based on real-time stats and historical data. Built for cricket enthusiasts, analysts, and tech enthusiasts alike! 🎉

Here is the demo of the IPL prediction model :

https://github.com/user-attachments/assets/cd2a01f3-aa96-474d-934f-d82eed6967d5
  

## 📋Project Goals

1. Predict IPL Match Winners: Use historical match data and real-time stats to calculate probabilities.
2. User-Friendly Web App: A sleek Flask-based interface for interactive predictions.
3. Deploy for Public Access: Share predictions with the world via Render.


## 🔍Features
**1. Model Training:**

- Algorithms Used:
  - Logistic Regression
  - Random Forest Classifier (🌟 Best with **99% accuracy**)
  - Gradient Boosting Classifier
- Key Features in the Model:
  -  Team Details: *BattingTeam, BowlingTeam*
  - Match Stats: *Runs left, Balls left, Wickets remaining*
  - Targets: *Target Runs, Current Run Rate (CRR), Required Run Rate (RRR)*
  -  Match Metadata: *Venue, Toss Winner*

**2. Web Application:**

- Input: Match details like teams, venue, and in-match stats.
- Output: Probabilities of each team winning, displayed as progress bars for visual clarity.
- Real-time and interactive predictions! 🚀

**3. Deployment**

**URL:** Visit the App on Render [Visit Live App](https://ipl-winning-team-prediction.onrender.com)


*(Note: May take a moment to wake up if idle.)*





## 🗂️ Repository File Details

The repository is structured as follows:

| File/Directory                          | Description                                                                                 |
|-----------------------------------------|---------------------------------------------------------------------------------------------|
| `app.py`                                | The Flask application handling user input and prediction results.                           |
| `templates/`                            | Folder containing HTML templates.                                                          |
| &nbsp;&nbsp;├── `index.html`            | The homepage where users can input match details.                                           |
| &nbsp;&nbsp;└── `result.html`           | The result page displaying prediction probabilities and outcomes.                           |
| `static/`                               | Folder containing static assets (CSS and images).                                           |
| &nbsp;&nbsp;├── `style.css`             | CSS file for general styling of the web application.                                        |
| &nbsp;&nbsp;├── `restyle.css`           | CSS file specifically for styling the `result.html` page.                                   |
| &nbsp;&nbsp;└── `background-img.webp`   | Image used as the background for the web application's HTML pages.                          |
| `model.pkl`                             | Serialized trained machine learning model used in the Flask app.                            |
| `requirements.txt`                      | List of Python dependencies required to run the project.                                    |
| `Final_IPL_winner_prediction.ipynb`     | Jupyter Notebook containing the model training code.                                        |
| `all_season_details.zip`                | Dataset containing detailed historical IPL match data.                                      |
| `all_season_summary.zip`                | Dataset containing summary statistics of IPL matches.                                       |
| `README.md`                             | Project documentation and setup guidelines.                                                 |

---

### **Dataset Details**
- The datasets `all_season_details.zip` and `all_season_summary.zip` were merged to create the training data for the model.  
- Key features extracted from the merged dataset include:  
  - *BattingTeam*, *BowlingTeam*, *Runs left*, *Balls left*, *Wickets remaining*, *Venue*, *Toss Winner*, etc.  

## 🚀 Getting Started

**1. Prerequisites:**

- Python 3.7+
- Pip
- Git

**2. Clone the Repository**

To clone the repository, run:

```git clone https://github.com/your-username/ipl-match-winner-prediction.git```

```cd ipl-match-winner-prediction```

**3. Install Dependencies**

Install the required Python packages:

```pip install -r requirements.txt```

**4. Run the Application**

Start the Flask application:

```python app.py```

**5. Access the App:**

Open your browser and navigate to http://127.0.0.1:5000/.

Input match details to view predictions.

## 🧠 How It Works

**1. Input Match Details:**
Provide details like batting team, bowling team, venue, runs left, etc.

**2. Preprocessing:**
Data is scaled and transformed for optimal model performance.

**3. Prediction:**
The trained model calculates the probability of each team winning.

## 🤝 Contributing:
- Fork the repo.
- Submit a pull request with your changes.
- Suggestions and feature requests are always welcome! 💡


## 🌟 Ready to Play?
- **Visit Live App:** IPL Winning Team Prediction
- Join the cricket tech revolution today! 🏏✨
