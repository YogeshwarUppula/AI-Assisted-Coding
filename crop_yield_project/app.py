"""
Crop Yield Prediction Web App
Course: AI-Assisted Coding

This Flask-based application takes environmental & soil parameters
from a webpage and checks them against a dataset to predict crop yield.
The system also stores last 5 predictions into a CSV file.
"""

from flask import Flask, render_template, request
import pandas as pd
import csv, os

# Initialize Flask application
app = Flask(__name__)

# Load dataset containing agriculture data
df = pd.read_csv("data/sample_data.csv")

# Extract soil types to show in dropdown (unique sorted list)
soil_types = sorted(df["Soil_Type"].unique())


@app.route('/')
def home():
    """Home route: loads input form and recent prediction history"""
    
    history = []
    history_path = "data/history.csv"

    # Check if history file exists → load last 5 predictions
    if os.path.exists(history_path):
        history = pd.read_csv(history_path).tail(5).to_dict(orient="records")

    # Send soil types + history to webpage
    return render_template('index.html', soil_options=soil_types, history=history)


@app.route('/predict', methods=['POST'])
def predict():
    """Reads user input → matches dataset → predicts crop yield"""

    # Fetch input values from HTML form
    soil = request.form['soil_type']
    ph = float(request.form['ph'])
    moisture = float(request.form['moisture'])
    temp = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    rainfall = float(request.form['rainfall'])

    # Filter dataset for exact match of all input values
    matched = df[
        (df["Soil_Type"] == soil) &
        (df["Soil_pH"] == ph) &
        (df["Soil_Moisture"] == moisture) &
        (df["Temperature"] == temp) &
        (df["Humidity"] == humidity) &
        (df["Rainfall"] == rainfall)
    ]

    # If row exists in dataset → take prediction value
    if not matched.empty:
        result = round(matched["Crop_Yield"].values[0], 3)

        # Save input & prediction to history CSV
        history_path = "data/history.csv"
        file_exists = os.path.isfile(history_path)

        with open(history_path, "a", newline="") as f:
            writer = csv.writer(f)

            # Write header if file created newly
            if not file_exists:
                writer.writerow(["Soil", "pH", "Moisture", "Temp", "Humidity", "Rainfall", "Yield"])

            writer.writerow([soil, ph, moisture, temp, humidity, rainfall, result])

        # Create formatted message for display
        prediction_text = f"""
        🌱 <b>Prediction Details</b><br><br>
        <b>Soil:</b> {soil}<br>
        <b>pH:</b> {ph}<br>
        <b>Moisture:</b> {moisture}%<br>
        <b>Temperature:</b> {temp} °C<br>
        <b>Humidity:</b> {humidity}%<br>
        <b>Rainfall:</b> {rainfall} mm<br><br>

        <b>Final Crop Yield:</b><br>
        <span class='highlight'>{result} tons/hectare 🌾</span>
        """
    else:
        # No matching dataset row found
        prediction_text = "⚠️ No exact match found in dataset!"

    # Reload updated history for display
    history = pd.read_csv("data/history.csv").tail(5).to_dict(orient="records")

    # Pass values back to webpage
    return render_template(
        'index.html',
        soil_options=soil_types,
        prediction_value=prediction_text,
        history=history
    )


# Start Flask development server
if __name__ == "__main__":
    app.run(debug=True)
