import numpy as np
import pickle
import streamlit as st

load_model = pickle.load(open('model.pkl', 'rb'))

def predict(input_data):
   
    if input_data == 0:
        return 'Customer stayed'
    else:
        return 'Customer churned'


def main():
    # Title
    st.title("Customer Churn Prediction WebApp")

    # fetching the input data from the user
    
    Age = st.text_input('Enter age')
    Location = st.text_input('Enter location')
    Subscription_Length_Months = st.text_input('Enter length of subscription months')
    Monthly_Bill = st.text_input('Enter monthly bill')
    Total_Usage_GB = st.text_input('Enter total GB used')

    # prediction part
    churn = ''

    # creating button for prediction
    if st.button('Predict'):
        churn = predict([[Age, Location, Subscription_Length_Months, Monthly_Bill, Total_Usage_GB]])
        st.success(churn)

if __name__ == "__main__":
    main()

# import pickle
# import streamlit as st

# load_model = pickle.load(open('model.sav', 'rb'))

# def predict(input_data):
#     return load_model.predict(input_data)

# def main():
#     # Title
#     st.title("Customer Churn Prediction WebApp")

#     # fetching the input data from the user
#     Age = st.text_input('Enter age')
#     Location = st.text_input('Enter location')
#     Subscription_Length_Months = st.text_input('Enter length of subscription months')
#     Monthly_Bill = st.text_input('Enter monthly bill')
#     Total_Usage_GB = st.text_input('Enter total GB used')

#     # prediction part
#     prediction_data = [[Age,Location, Subscription_Length_Months, Monthly_Bill, Total_Usage_GB]]

#     # creating button for prediction
#     if st.button('Predict'):
#         churn = predict(prediction_data)

#         if churn == 0:
#             st.success('Customer stayed')
#         else:
#             st.error('Customer churned')

# if __name__ == "__main__":
#     main()


# import pickle
# import streamlit as st
# from sklearn.preprocessing import LabelEncoder

# # Load the model
# load_model = pickle.load(open('model.sav', 'rb'))

# # Load the label encoder (assuming it's been pickled during training)
# label_encoder = pickle.load(open('label_encoder.sav', 'rb'))

# def predict(input_data):
#     return load_model.predict(input_data)

# def main():
#     # Title
#     st.title("Customer Churn Prediction WebApp")

#     # Fetching the input data from the user
#     Age = int(st.text_input('Enter age'))
#     Location = st.text_input('Enter location')
#     Subscription_Length_Months = int(st.text_input('Enter length of subscription months'))
#     Monthly_Bill = float(st.text_input('Enter monthly bill'))
#     Total_Usage_GB = float(st.text_input('Enter total GB used'))

#     # Transform categorical variables using the label encoder
#     Location_encoded = label_encoder.transform([Location])

#     # Create the prediction data array
#     prediction_data = [[Age, Location_encoded[0], Subscription_Length_Months, Monthly_Bill, Total_Usage_GB]]

#     # Create button for prediction
#     if st.button('Predict'):
#         churn = predict(prediction_data)

#         if churn == 0:
#             st.success('Customer stayed')
#         else:
#             st.error('Customer churned')

# if __name__ == "__main__":
#     main()




# import pickle
# import streamlit as st

# # Load the model
# load_model = pickle.load(open('model.sav', 'rb'))

# # Load the label encoder
# label_encoder = pickle.load(open('one_encoder.sav', 'rb'))

# def predict(input_data):
#     return load_model.predict(input_data)

# def main():
#     # Title
#     st.title("Customer Churn Prediction WebApp")

#     # Fetching the input data from the user
#     Age = st.text_input('Enter age')
#     Subscription_Length_Months = st.text_input('Enter length of subscription months')
#     Monthly_Bill = st.text_input('Enter monthly bill')
#     Total_Usage_GB = st.text_input('Enter total GB used')

#     try:
#         # Validate and convert inputs to appropriate types
#         Age = int(Age)
#         Subscription_Length_Months = int(Subscription_Length_Months)
#         Monthly_Bill = float(Monthly_Bill)
#         Total_Usage_GB = float(Total_Usage_GB)

#         # Input validation for Location is still needed
#         Location = st.text_input('Enter location')

#         # Transform categorical variables using the label encoder
#         Location_encoded = label_encoder.transform([Location])

#         # Create the prediction data array
#         prediction_data = [[Age, Location_encoded[0], Subscription_Length_Months, Monthly_Bill, Total_Usage_GB]]

#         # Create button for prediction
#         if st.button('Predict'):
#             churn = predict(prediction_data)

#             if churn == 0:
#                 st.success('Customer stayed')
#             else:
#                 st.error('Customer churned')

#     except ValueError:
#         st.error("Please enter valid numeric values for age, subscription length, monthly bill, and total usage.")

# if __name__ == "__main__":
#     main()




# import pickle
# import streamlit as st
# import numpy as np

# # Load the model
# load_model = pickle.load(open('model.sav', 'rb'))

# # Load the label encoder
# label_encoder = pickle.load(open('label_encoder.sav', 'rb'))

# def predict(input_data):
#     return load_model.predict(input_data)

# def main():
#     # Title
#     st.title("Customer Churn Prediction WebApp")

#     # Fetching the input data from the user
#     Age = st.text_input('Enter age')
#     Subscription_Length_Months = st.text_input('Enter length of subscription months')
#     Monthly_Bill = st.text_input('Enter monthly bill')
#     Total_Usage_GB = st.text_input('Enter total GB used')
#     Location = st.text_input('Enter location')

#     # Check if all input fields are non-empty before validation and conversion
#     if Age and Subscription_Length_Months and Monthly_Bill and Total_Usage_GB:
#         try:
#             # Validate and convert inputs to appropriate types
#             Age = int(Age)
#             Subscription_Length_Months = int(Subscription_Length_Months)
#             Monthly_Bill = float(Monthly_Bill)
#             Total_Usage_GB = float(Total_Usage_GB)

#             # Transform categorical variables using the label encoder
#             Location_encoded = label_encoder.transform([Location])

#             # Create the prediction data array
#             prediction_data = [[Age, Location_encoded[0], Subscription_Length_Months, Monthly_Bill, Total_Usage_GB]]

#             # Create button for prediction
#             if st.button('Predict'):
#                 churn = predict(prediction_data)

#                 if churn == 0:
#                     st.success('Customer stayed')
#                 else:
#                     st.error('Customer churned')

#         except ValueError:
#             st.error("Please enter valid numeric values for age, subscription length, monthly bill, and total usage.")

# import pickle
# import streamlit as st
# import numpy as np

# # Load the model
# load_model = pickle.load(open('model.sav', 'rb'))

# # Load the label encoder
# label_encoder = pickle.load(open('one_encoder.sav', 'rb'))

# def predict(input_data):
#     return load_model.predict(input_data)

# def main():
#     # Title
#     st.title("Customer Churn Prediction WebApp")

#     # Fetching the input data from the user
#     Age = st.text_input('Enter age')
#     Subscription_Length_Months = st.text_input('Enter length of subscription months')
#     Monthly_Bill = st.text_input('Enter monthly bill')
#     Total_Usage_GB = st.text_input('Enter total GB used')
#     Location = st.text_input('Enter location')

#     # Convert the input data to appropriate data types
#     try:
#         Age = int(Age)
#         Subscription_Length_Months = int(Subscription_Length_Months)
#         Monthly_Bill = float(Monthly_Bill)
#         Total_Usage_GB = float(Total_Usage_GB)

#         # Transform categorical variables using the label encoder
#         Location_encoded = label_encoder.transform([Location])

#         # Create the prediction data array
#         prediction_data = np.array([[Age, Location_encoded[0], Subscription_Length_Months, Monthly_Bill, Total_Usage_GB]])

#         # Create button for prediction
#         if st.button('Predict'):
#             churn = predict(prediction_data)

#             if churn == 0:
#                 st.success('Customer stayed')
#             else:
#                 st.error('Customer churned')

#     except ValueError:
#         st.error("Please enter valid numeric values for age, subscription length, monthly bill, and total usage.")

# if __name__ == "__main__":
#     main()
