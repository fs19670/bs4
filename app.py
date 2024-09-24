import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# Load dataset from the specified path
dataset = pd.read_csv('C:\\New folder\\sale_prediction_ml_logistic_regression.csv')

st.markdown('<h1 style="color:purple;">Sale Prediction using logistic regression</h1>', unsafe_allow_html=True)
# st.header('Sale Prediction using logistic regression')
# Display text with color using Markdown and HTML
# st.markdown('<p style="color:blue; font-size:20px;">Sale Prediction using logistic regression.</p>', unsafe_allow_html=True)

# Display dataset shape and first 5 rows
st.write("Dataset Shape: ", dataset.shape)
st.write("First 5 rows of the dataset:")
st.write(dataset.head(5))

# Splitting dataset into features (X) and target (Y)
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

# Splitting Dataset into Train & Test
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the Logistic Regression model
model = LogisticRegression(random_state=0)
model.fit(X_train, y_train)

# Streamlit inputs for new customer data
st.header("Predict if a Customer will Buy")
age = st.number_input("Enter Customer Age", min_value=18, max_value=100, value=30)
sal = st.number_input("Enter Customer Salary", min_value=15000, max_value=200000, value=50000)

if st.button('Predict'):
    newCust = [[age, sal]]
    result = model.predict(sc.transform(newCust))
    
    if result == 1:
        st.success("Customer will Buy")
    else:
        st.error("Customer won't Buy")

# Predicting the test set results
y_pred = model.predict(X_test)

# Display predicted vs actual results
st.subheader("Predicted vs Actual Results")
st.write(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

# Confusion Matrix and Accuracy
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred) * 100

st.subheader("Model Performance")
st.write("Confusion Matrix: ")
st.write(cm)
st.write(f"Accuracy of the Model: {accuracy:.2f}%")
