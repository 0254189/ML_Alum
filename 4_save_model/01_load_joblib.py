import joblib
<<<<<<< HEAD


# model_path = "model_joblib"
model_path = "4_save_model/model_joblib"
mj = joblib.load(model_path)

print(mj.predict([[2020]]))
=======
import os

model = os.path.join(os.path.dirname(__file__), 'model_joblib')

model_path = 'model_joblib'
mj = joblib.load(model)

print(mj.predict([[2020]]))
>>>>>>> 832255d7195343c4872791bda44df2ff23e1e1aa
