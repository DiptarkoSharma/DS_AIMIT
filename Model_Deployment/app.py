from flask import Flask, render_template, request
import numpy as np
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the model
with open('model_pickle', 'rb') as model_file:
    model = pickle.load(model_file)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get inputs from the form
    area = float(request.form['area'])
    bedrooms = float(request.form['bedrooms'])
    age = float(request.form['age'])

    # Create input array for the model
    inputs = np.array([area, bedrooms, age]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(inputs)

    # Return the result
    return render_template('index.html', prediction_text=f'Prediction: {round(prediction[0])}')

if __name__ == '__main__':
    app.run(debug=True)
