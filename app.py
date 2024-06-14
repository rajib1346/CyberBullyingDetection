from flask import Flask, request, render_template
import pickle

# Load the trained model
with open('cyberbullying_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        try:
            tweet = request.form['tweet']
            prediction = model.predict([tweet])[0]
        except Exception as e:
            print(f"Error: {e}")
    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)