import numpy as np
import pickle

loaded_model = pickle.load(open('C:/Users\gugan/OneDrive/Documents/codeclouse_internship/Treained_model.sav', 'rb'))

input_data = (57,0,0,140,241,0,1,123,0,0.2,1,0,3)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshape = input_data_as_numpy_array.reshape(1,-1)
prediction = loaded_model.predict(input_data_reshape)
print(prediction)
if(prediction[0]==0):
    print("The person has Heart Disease")
else:
    print("The person does not have heart disease")
    