# 🌾 Crop Yield Prediction Using Machine Learning

## 📌 Project Overview

This project is a Machine Learning based web application that predicts crop yield based on various environmental and agricultural factors.
It uses a Decision Tree Regression model and a Flask web interface where users can input details like crop type, rainfall, temperature, and other parameters to get a predicted yield.

## 🚀 Features

* Predict crop yield using ML model
* User-friendly Flask web interface
* Data preprocessing using:

  * StandardScaler
  * OneHotEncoder
  * ColumnTransformer
* Fast real-time prediction
* Clean project structure

## 🧠 Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* HTML/CSS

## 📂 Project Structure

```
Crop-Yield-Prediction-Using-ML/
│
├── app.py
├── dtr.pkl
├── requirements.txt
├── templates/
│     └── index.html
├── static/
└── README.md
```

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/Crop-Yield-Prediction-Using-ML.git
cd Crop-Yield-Prediction-Using-ML
```

### 2️⃣ Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the application

```
python app.py
```

### 5️⃣ Open in browser

```
http://127.0.0.1:5000
```

## 📊 How It Works

1. User enters crop details in the web form
2. Data is preprocessed using saved transformers
3. Decision Tree model predicts crop yield
4. Result is displayed instantly on the webpage

## 🧪 Model Details

* Algorithm: Decision Tree Regressor
* Preprocessing:

  * Scaling for numeric data
  * One-hot encoding for categorical data

## 📸 Screenshot

(Add a screenshot of your app here after uploading to GitHub)

## 📈 Future Improvements

* Deploy on cloud (Render/Heroku)
* Add more ML models for comparison
* Improve UI design
* Add accuracy metrics
* Connect with real-time agricultural datasets

## 👨‍💻 Author

**Arjun**
BTech CSE Student

## ⭐ If you like this project

Give it a star on GitHub!
