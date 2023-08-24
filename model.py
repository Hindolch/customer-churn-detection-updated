import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pickle 


load_model = pickle.load(open('model.pkl', 'rb'))


y_pred_test = load_model.predict([[20,'Miami',10,42.45,150]])
if y_pred_test == 1:
    print('Customer churned')
else:
    print('Customer stayed')