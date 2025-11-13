import joblib
import os

print("-" * 50)
print(__file__)
print("-" * 50)

model_path = os.path.join(os.path.dirname(__file__), "model_joblib")
mj = joblib.load(model_path)

print(mj.predict([[2020]]))
