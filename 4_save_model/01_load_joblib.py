import joblib
import os

model = os.path.join(os.path.dirname(__file__), 'model_joblib')

model_path = 'model_joblib'
mj = joblib.load(model)

print(mj.predict([[2020]]))