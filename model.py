from pathlib import Path
import joblib,pandas as pd
MODEL=Path(__file__).parent/"models"/"house_price_model.joblib"
class HousePriceModel:
    def __init__(self,path=MODEL):
        if not path.exists(): raise FileNotFoundError("Model not found. Run python train.py")
        self.model=joblib.load(path)
    def predict(self,features):
        return float(self.model.predict(pd.DataFrame([features]))[0])
