# Crop Yield Prediction
This project is a web-based application that predicts the crop yield using soil and environmental conditions.  
The user enters the details such as pH, moisture, temperature, humidity, rainfall, and soil type.  
Based on the given input, the system checks the dataset and displays the expected crop yield per hectare.

This project is developed under the course **AI-Assisted Coding** as a simple application of data-driven agriculture.

---
## Project Objective

To assist farmers and agricultural planners in estimating crop productivity using soil and climate inputs.  
This helps in better crop planning and resource management.

---

## Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python | Backend logic |
| Flask | Web framework for UI and routing |
| HTML + CSS | Frontend interface |
| Pandas | Dataset filtering |
| CSV | Data storage |

---

## Dataset Used

File: `sample_data.csv`  
Contains the following columns:

- Soil_Type  
- Soil_pH  
- Soil_Moisture  
- Temperature  
- Humidity  
- Rainfall  
- Crop_Yield (tons/hectare)

The system checks the input values against this dataset and produces the corresponding crop yield value.

---

---

## Input Fields

The user must provide:

| Field | Description |
|-------|-------------|
| Soil Type | Select from dropdown |
| Soil pH | Acidity / alkalinity of soil |
| Soil Moisture (%) | Water content in soil |
| Temperature (°C) | Atmospheric temperature |
| Humidity (%) | Water vapor amount in air |
| Rainfall (mm) | Monthly average rainfall |

---

## Sample Input

| Parameter | Value |
|----------|-------|
| Soil Type | Sandy |
| Soil pH | 5.9 |
| Soil Moisture | 24.1 |
| Temperature | 26.1 |
| Humidity | 51.3 |
| Rainfall | 95.5 |

---

## Sample Output
Soil: Sandy
pH: 5.9
Moisture: 24.1 %
Temperature: 26.1 °C
Humidity: 51.3 %
Rainfall: 95.5 mm

Crop Yield: 3.84 tons/hectare

---

## How to Run the Project

> Make sure Python 3 is installed.

### Step 1: Install required libraries
pip install flask pandas

### Step 2: Go to the project folder
cd crop_yield_project

### Step 3: Run the application
python app.py

### Step 4: Open the web page  


