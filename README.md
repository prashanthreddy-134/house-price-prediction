# 🏠 House Price Prediction

A machine learning project that predicts house prices based on property characteristics such as area, number of bedrooms, bathrooms, property age, parking availability, and location.

The project includes a complete end-to-end machine learning workflow with model training, model comparison, saved model deployment, and an interactive Streamlit web application.

---

## 🚀 Project Overview

House price prediction is a supervised machine learning regression problem.

This project analyzes property features and predicts the estimated house price.

The application allows users to enter property information and receive an estimated house price through an interactive web interface.

The project demonstrates how machine learning can be used to build a practical real-estate price prediction application.

---

## ✨ Features

### Machine Learning

- Regression-based house price prediction
- Data preprocessing
- Feature preparation
- Categorical feature handling
- Train/test split
- Multiple model comparison
- Model evaluation
- Best-model selection
- Model serialization using Joblib

### Web Application

- Streamlit interface
- Interactive property inputs
- House price prediction
- Location selection
- Property feature inputs
- Estimated price display
- Professional dashboard-style interface

---

# 📊 Model Comparison

Multiple machine learning regression algorithms were evaluated.

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 359,921.98 | 455,681.12 | 0.9953 |
| Decision Tree | 971,004.74 | 1,229,576.17 | 0.9659 |
| Random Forest | 706,141.80 | 889,037.43 | 0.9822 |
| Gradient Boosting | 515,687.44 | 633,120.75 | 0.9910 |

The trained project uses the selected **Linear Regression** model, which is saved as:

```text
models/house_price_model.joblib
```

The metrics above are results from this project's dataset and evaluation setup and should not be interpreted as real-world property-market accuracy.

---

# 🧠 Machine Learning Workflow

```text
House Dataset
      ↓
Data Loading
      ↓
Data Preprocessing
      ↓
Feature Preparation
      ↓
Categorical Encoding
      ↓
Train/Test Split
      ↓
Model Training
      ↓
Model Comparison
      ↓
Model Evaluation
      ↓
Best Model Selection
      ↓
Model Serialization
      ↓
Streamlit Application
      ↓
House Price Prediction
```

---

# 📁 Dataset

The dataset is located at:

```text
data/houses.csv
```

The dataset contains the following features:

| Feature | Description |
|---|---|
| `area_sqft` | Property area in square feet |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `age` | Approximate property age |
| `parking` | Parking availability/count |
| `location` | Property location |
| `price` | Target house price |

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib
- Machine Learning
- Git
- GitHub

---

# 📂 Project Structure

```text
House_Price_Prediction/
│
├── data/
│   └── houses.csv
│
├── models/
│   └── house_price_model.joblib
│
├── app.py
├── model.py
├── train.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 💻 Requirements

Before running the project, make sure you have:

- Python 3.10 or newer
- pip
- Git
- VS Code (recommended)

Check Python:

```powershell
python --version
```

Check pip:

```powershell
pip --version
```

---

# 📥 Clone the Repository

Clone the project:

```powershell
git clone https://github.com/prashanthreddy-134/house-price-prediction.git
```

Move into the project:

```powershell
cd house-price-prediction
```

---

# 🐍 Create a Virtual Environment

Create a virtual environment:

```powershell
python -m venv .venv
```

---

# ▶️ Activate Virtual Environment

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell displays an execution-policy error, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

---

# 📦 Install Dependencies

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install project dependencies:

```powershell
pip install -r requirements.txt
```

---

# 🏋️ Train the Model

To train the machine learning models:

```powershell
python train.py
```

The training script:

1. Loads the house dataset.
2. Prepares the input features.
3. Separates the target variable.
4. Splits the data into training and testing sets.
5. Trains multiple regression algorithms.
6. Evaluates the models.
7. Compares their performance.
8. Selects the project model.
9. Saves the trained model.

The trained model is saved to:

```text
models/house_price_model.joblib
```

---

# 🌐 Run the Streamlit Application

Start the application:

```powershell
python -m streamlit run app.py
```

Streamlit will display a local address similar to:

```text
http://localhost:8501
```

Open the displayed URL in your browser.

---

# ⚡ Quick Start

If Python is already installed:

```powershell
git clone https://github.com/prashanthreddy-134/house-price-prediction.git
cd house-price-prediction
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m streamlit run app.py
```

---

# 🪟 Complete Windows PowerShell Setup

Run these commands one at a time:

```powershell
git clone https://github.com/prashanthreddy-134/house-price-prediction.git
```

```powershell
cd house-price-prediction
```

```powershell
python -m venv .venv
```

```powershell
.\.venv\Scripts\Activate.ps1
```

```powershell
pip install -r requirements.txt
```

```powershell
python -m streamlit run app.py
```

---

# 🖥️ Using the Application

After opening the Streamlit application:

1. Enter the property area.
2. Select the number of bedrooms.
3. Enter the number of bathrooms.
4. Enter the property age.
5. Enter parking information.
6. Select the property location.
7. Submit the prediction.
8. The application calculates an estimated house price.

The result is a machine learning estimate based on the project's training dataset.

---

# 🏡 Example Prediction

Example property:

```text
Area       : 1500 sq ft
Bedrooms   : 3
Bathrooms  : 2
Age        : 10 years
Parking    : 1
Location   : Bengaluru
```

The trained application produces an estimated property price based on the learned model.

Because the dataset is an educational dataset, the prediction should not be interpreted as a professional real-estate valuation.

---

# 🧠 Model Architecture

The project uses a regression pipeline for predicting continuous house prices.

The model receives property features such as:

```text
Area
Bedrooms
Bathrooms
Age
Parking
Location
```

and produces:

```text
Estimated House Price
```

The trained model is serialized with Joblib and loaded by the Streamlit application.

---

# 📄 Important Files

## `app.py`

Main Streamlit application.

Responsible for:

- User interface
- Property inputs
- Loading the trained model
- Prediction
- Displaying estimated price

---

## `model.py`

Contains model-related functionality used by the application.

---

## `train.py`

Machine learning training script.

Responsible for:

- Dataset loading
- Data preparation
- Feature processing
- Model training
- Model evaluation
- Model comparison
- Saving the trained model

---

## `data/houses.csv`

House/property dataset used for model training and evaluation.

---

## `models/house_price_model.joblib`

Serialized trained machine learning model.

---

## `requirements.txt`

Contains the Python dependencies required to run the project.

---

# 📈 Evaluation Metrics

The project evaluates regression models using:

### MAE — Mean Absolute Error

Measures the average absolute difference between actual and predicted prices.

```text
MAE = Average absolute prediction error
```

Lower values indicate smaller average absolute errors on the evaluation data.

---

### RMSE — Root Mean Squared Error

Measures prediction error while giving greater weight to larger errors.

```text
RMSE = Square root of mean squared error
```

Lower values indicate smaller errors on the evaluation data.

---

### R² Score

Measures how much of the target variation is explained by the model on the evaluation data.

Higher values indicate a better fit under that evaluation setup.

---

# 🔄 Retraining the Model

To retrain the model:

```powershell
python train.py
```

After training, check the model directory:

```powershell
Get-ChildItem .\models\
```

You should see:

```text
house_price_model.joblib
```

Then launch the application:

```powershell
python -m streamlit run app.py
```

---

# 🔧 Troubleshooting

## Python is not recognized

Check:

```powershell
python --version
```

If Python is not installed or not available in PATH, install Python and restart the terminal.

---

## pip is not recognized

Try:

```powershell
python -m pip --version
```

Then:

```powershell
python -m pip install -r requirements.txt
```

---

## Streamlit is not recognized

Use:

```powershell
python -m streamlit run app.py
```

instead of:

```powershell
streamlit run app.py
```

---

## ModuleNotFoundError

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then install dependencies:

```powershell
pip install -r requirements.txt
```

---

## Model file not found

Check:

```powershell
Get-ChildItem .\models\
```

If the model is missing, run:

```powershell
python train.py
```

---

## PowerShell Execution Policy Error

Run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

# 🛑 Stop the Application

To stop Streamlit:

```text
Ctrl + C
```

---

# 🧹 Remove Python Cache

Python may create `__pycache__` directories while running the project.

They are excluded from GitHub using `.gitignore`.

To remove them manually:

```powershell
Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
```

---

# 🔐 GitHub Workflow

Check project status:

```powershell
git status
```

Stage changes:

```powershell
git add .
```

Create a commit:

```powershell
git commit -m "Update house price prediction project"
```

Push changes:

```powershell
git push
```

---

# 📌 GitHub Repository

Repository:

```text
https://github.com/prashanthreddy-134/house-price-prediction
```

Clone:

```powershell
git clone https://github.com/prashanthreddy-134/house-price-prediction.git
```

---

# 🔮 Future Improvements

Possible improvements include:

- Larger real-world datasets
- Additional geographical features
- Advanced feature engineering
- Hyperparameter optimization
- Cross-validation
- XGBoost regression
- LightGBM regression
- CatBoost regression
- Model comparison dashboard
- Feature importance visualization
- SHAP explainability
- Interactive price analysis
- Geographic visualization
- Real-estate market trend analysis
- REST API deployment
- Cloud deployment
- Database integration
- Automated model retraining
- Production monitoring

---

# ⚠️ Limitations

This project is designed for educational, demonstration, and portfolio purposes.

Predictions depend on:

- Dataset quality
- Dataset size
- Feature availability
- Training data distribution
- Model assumptions
- Input values

The dataset used in this project is not sufficient for professional property valuation.

Predicted prices should therefore be treated as machine learning estimates rather than guaranteed market prices or financial advice.

---

# 🎯 Learning Objectives

This project demonstrates practical experience with:

- Regression
- Supervised machine learning
- Data preprocessing
- Feature engineering
- Categorical data handling
- Model comparison
- Regression evaluation metrics
- Model serialization
- Python development
- Streamlit development
- Git
- GitHub
- End-to-end ML application development

---

# 👨‍💻 Author

**Prashanth Reddy S**

BE – Information Science & Engineering

GitHub:

```text
https://github.com/prashanthreddy-134
```

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is provided for educational and portfolio purposes.