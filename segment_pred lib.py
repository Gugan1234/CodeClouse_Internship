import numpy as np
import pickle

load_model = pickle.load(open('C:/Users\gugan/OneDrive/Documents/codeclouse_internship/Train_model.sav','rb'))
input_data = (1,20,15,87)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshape = input_data_as_numpy_array.reshape(1,-1)
prediction = load_model.predict(input_data_reshape)
print(prediction)
if (prediction[0] == 1):
    print("The customer belongs to 1th crew")
if (prediction[0] == 2):
    print("The customer belongs to 2th crew")
if (prediction[0] == 3):
    print("The customer belongs to 3th crew")
if (prediction[0] == 4):
    print("The customer belongs to 4th crew")
if (prediction[0] == 5):
    print("The customer belongs to 5th crew")