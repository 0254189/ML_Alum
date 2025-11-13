import pickle

with open("4_save_model/model_pickle", "rb") as file:
    mp = pickle.load(file)

print(mp.predict([[2020]]))
