import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# -----------------------------
# 1. Load dataset
# -----------------------------
DATA_PATH = "data/houses.csv"
MODEL_PATH = "models/house_price_model.joblib"

df = pd.read_csv(DATA_PATH)

# -----------------------------
# 2. Features and target
# -----------------------------
X = df.drop("price", axis=1)
y = df["price"]

categorical_features = ["location"]
numeric_features = [
    "area_sqft",
    "bedrooms",
    "bathrooms",
    "age",
    "parking"
]

# -----------------------------
# 3. Preprocessing
# -----------------------------
preprocessor = ColumnTransformer(
    transformers=[
        (
            "location",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

# -----------------------------
# 4. Train/test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# -----------------------------
# 5. Models
# -----------------------------
models = {
    "Linear Regression": LinearRegression(),

    "Decision Tree": DecisionTreeRegressor(
        random_state=42,
        max_depth=12
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=300,
        random_state=42,
        n_jobs=-1
    ),

    "Gradient Boosting": GradientBoostingRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=3,
        random_state=42
    )
}

# -----------------------------
# 6. Train and evaluate
# -----------------------------
results = []

best_model = None
best_r2 = float("-inf")
best_model_name = None

for name, model in models.items():

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    rmse = mean_squared_error(
        y_test,
        predictions
    ) ** 0.5

    r2 = r2_score(
        y_test,
        predictions
    )

    results.append({
        "Model": name,
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    })

    print(f"\n{name}")
    print(f"MAE:  {mae:,.2f}")
    print(f"RMSE: {rmse:,.2f}")
    print(f"R2:   {r2:.4f}")

    if r2 > best_r2:
        best_r2 = r2
        best_model = pipeline
        best_model_name = name


# -----------------------------
# 7. Model comparison
# -----------------------------
results_df = pd.DataFrame(results)

print("\n" + "=" * 55)
print("MODEL COMPARISON")
print("=" * 55)

print(
    results_df.to_string(
        index=False,
        formatters={
            "MAE": "{:,.2f}".format,
            "RMSE": "{:,.2f}".format,
            "R2": "{:.4f}".format
        }
    )
)

print("\nBest model:", best_model_name)
print(f"Best R2: {best_r2:.4f}")


# -----------------------------
# 8. Save best model
# -----------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(
    best_model,
    MODEL_PATH
)

print(f"\nSaved best model to: {MODEL_PATH}")