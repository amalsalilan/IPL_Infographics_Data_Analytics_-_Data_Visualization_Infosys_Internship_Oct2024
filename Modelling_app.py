{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "128f7f28-c9d1-44d0-ba32-fedfc33bcd3f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: Could not find a version that satisfies the requirement jupyter-streamlit (from versions: none)\n",
      "ERROR: No matching distribution found for jupyter-streamlit\n"
     ]
    }
   ],
   "source": [
    "pip install jupyter-streamlit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a065c304-3310-48e1-9112-05c91a726d80",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-27 19:00:17.663 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Reshm\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import pandas as pd\n",
    "\n",
    "# Load the saved XGBoost model\n",
    "with open('xgb_model.pkl', 'rb') as f:\n",
    "    model = pickle.load(f)\n",
    "\n",
    "# App title\n",
    "st.title(\"IPL Run Prediction App\")\n",
    "\n",
    "# Sidebar for user input\n",
    "st.sidebar.header(\"Input Match Features\")\n",
    "over = st.sidebar.slider(\"Over\", 0, 20, 10)\n",
    "ball = st.sidebar.slider(\"Ball\", 0, 6, 3)\n",
    "run_rate = st.sidebar.number_input(\"Current Run Rate\", min_value=0.0, max_value=20.0, value=6.0, step=0.1)\n",
    "wickets_lost = st.sidebar.slider(\"Wickets Lost\", 0, 10, 2)\n",
    "\n",
    "# Prediction\n",
    "if st.sidebar.button(\"Predict\"):\n",
    "    # Create input DataFrame\n",
    "    input_data = pd.DataFrame({\n",
    "        'over': [over],\n",
    "        'ball': [ball],\n",
    "        'run_rate': [run_rate],\n",
    "        'wickets_lost': [wickets_lost]\n",
    "    })\n",
    "    \n",
    "    # Make prediction\n",
    "    prediction = model.predict(input_data)\n",
    "    \n",
    "    # Display prediction\n",
    "    st.write(f\"Predicted Cumulative Runs: {prediction[0]:.2f}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca0b8a9e-7d97-4ee0-b2b8-5738c6c01430",
   "metadata": {},
   "outputs": [],
   "source": [
    "streamlit run Modelling_app.py\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
