import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import pickle
import time

# Create an app object using the Flask class.
app = Flask(__name__)

# Load the trained model. (Pickle file)
model = pickle.load(open('models/model.pkl', 'rb'))

# Define the route to be home.
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for prediction.
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        message = request.form['news']
        start_time = time.time()
        pred = model.predict([message])  # Make sure to pass the message as a list
        prediction_time = round(time.time() - start_time, 4)
        print(pred)
        def predi(pred):
            if pred[0] == 1:
                res = "The statement is <span style='color: red;'>Cyber Bullying!</span>."
            else:
                res = "The statement is not <span style='color: green;'>Cyber Bullying.</span>"
            return res
        result = predi(pred)
        return render_template("prediction.html", prediction_text="{}".format(result), prediction_time=prediction_time)
    else:
        return render_template('prediction.html', prediction_text="Something went wrong", prediction_time="0")

if __name__ == "__main__":
    app.run(debug=False)
