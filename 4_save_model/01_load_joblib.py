import joblib


# model_path = "model_joblib"
model_path = "4_save_model/model_joblib"
mj = joblib.load(model_path)

print(mj.predict([[2020]]))
