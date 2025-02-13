# 🏡 Housing Price Predictor

This is a **Streamlit-based web application** that predicts house prices based on 13 key features using a trained Random Forest model.

## 🚀 Features
- User-friendly **web interface** built with Streamlit
- Takes **13 real estate features** as input
- Loads a **pre-trained Random Forest model**
- Provides an **instant price prediction**

## 📂 Project Structure
```
📁 House Price Predictor
│-- app.py                 # Streamlit application
│-- HousingPredictor.joblib # Trained ML model
│-- requirements.txt        # Dependencies
│-- README.md               # Documentation
```

## 🛠 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/housing-price-predictor.git
cd housing-price-predictor
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Application
```bash
streamlit run app.py
```

## 🎯 Usage
1. Enter values for the **13 housing features**.
2. Click the **Predict Price** button.
3. The estimated house price will be displayed.

## 🧪 Example Features
| Feature | Description |
|---------|------------|
| CRIM    | Crime rate per town |
| ZN      | Residential land proportion |
| INDUS   | Non-retail business acres |
| CHAS    | Proximity to the Charles River (0 or 1) |
| NOX     | Nitrogen oxide concentration |
| RM      | Average number of rooms |
| AGE     | Proportion of old buildings |
| DIS     | Distance to employment centers |
| RAD     | Accessibility to highways |
| TAX     | Property tax rate |
| PTRATIO | Pupil-teacher ratio |
| B       | Proportion of Black population |
| LSTAT   | Lower status population |

## 📌 Dependencies
- Python 3.7+
- Streamlit
- NumPy
- Scikit-learn
- Joblib


