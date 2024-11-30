from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import matplotlib.pyplot as plt
import tempfile
from statsmodels.tsa.stattools import adfuller
from itertools import product


def make_stationary(timeseries):
    differenced_series = timeseries.diff().dropna()  # Apply differencing
    return differenced_series, 1  # Return the differenced series and 1 difference applied


def find_best_arima_params(timeseries, p_range, d_range, q_range):
    best_aic = float("inf")
    best_order = None
    best_model = None

    for p, d, q in product(p_range, d_range, q_range):
        try:
            model = ARIMA(timeseries, order=(p, d, q))
            fitted_model = model.fit()
            if fitted_model.aic < best_aic:
                best_aic = fitted_model.aic
                best_order = (p, d, q)
                best_model = fitted_model
        except:
            continue  # Skip invalid models
    return best_order, best_model


def forecast_points(team_name, dataset_path, steps, p_range=range(0, 3), d_range=range(0, 2), q_range=range(0, 3)):
    try:
        # Load the dataset
        df = pd.read_csv(dataset_path)
        filter_data = df[df['name'] == team_name]

        if filter_data.empty:
            return f"No data found for the team '{team_name}'.", None

        # Prepare data
        filter_data = filter_data.sort_values('season').reset_index(drop=True)
        filter_data = filter_data[['season', 'matchpoints']]
        filter_data['season'] = pd.to_datetime(filter_data['season'], format='%Y')

        # Set the 'season' column as the index
        filter_data.set_index('season', inplace=True)

        # Ensure data starts from 2008
        filter_data = filter_data[filter_data.index.year >= 2008]

        # Make the time series stationary
        stationary_series, differences_applied = make_stationary(filter_data['matchpoints'])

        # Find the best p, d, q using grid search
        best_order, best_model = find_best_arima_params(stationary_series, p_range, d_range, q_range)
        if best_order is None:
            return "Could not find a suitable ARIMA model.", None

        # Forecast future points
        forecast = best_model.forecast(steps=steps)

        # Revert differencing if applied
        last_value = filter_data['matchpoints'].iloc[-1]
        if differences_applied > 0:
            forecast = forecast.cumsum() + last_value

        # Convert forecasted values to integers
        forecast = forecast.round().astype(int)

        # Prepare future season labels as integers
        last_season = filter_data.index[-1].year
        future_seasons = list(range(last_season + 1, last_season + 1 + steps))

        # Create results dictionary with integer values
        forecast_results = {f"Season {season}": points for season, points in zip(future_seasons, forecast)}

        # Save the plot as a temporary image file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
            plot_path = tmpfile.name
            plt.figure(figsize=(15, 7))
            
            # Plot historical data
            plt.plot(filter_data.index.year, filter_data['matchpoints'], label='Actual Data Points (2008-2023)', 
                     color='blue', marker='o', linestyle='-', linewidth=1.5)
            
            # Annotate historical data points (only the values)
            for x, y in zip(filter_data.index.year, filter_data['matchpoints']):
                plt.text(x, y + 1, f"{y:.2f}", fontsize=8, color="blue", ha='center')

            # Plot forecasted data
            plt.plot(future_seasons, forecast, label='Predicted Data Points (2024+)',
                     color='green', marker='o', linestyle='--', linewidth=1.5)

            # Annotate forecasted data points (only the values)
            for x, y in zip(future_seasons, forecast):
                plt.text(x, y + 1, f"{y:.2f}", fontsize=8, color="green", ha='center')

            # Add labels, title, legend, and grid
            plt.title(f"{team_name} Match Points Per Season", fontsize=14)
            plt.xlabel("Season", fontsize=12)
            plt.ylabel("Average Match Points", fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.xticks(range(2008, last_season + steps + 1))  # Ensure all seasons are displayed
            plt.legend(fontsize=10)
            plt.tight_layout()
            plt.savefig(plot_path)
            plt.close()

        return forecast_results, plot_path

    except Exception as e:
        return str(e), None
