from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('heart_attack_model.pkl')

@app.route('/')
def home():
    # Display the input form
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        age = float(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trtbps = float(request.form['trtbps'])
        chol = float(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalachh = float(request.form['thalachh'])
        exng = int(request.form['exng'])
        oldpeak = float(request.form['oldpeak'])
        slp = int(request.form['slp'])
        caa = int(request.form['caa'])
        thal = int(request.form['thal'])

        # Combine features into an array
        features = np.array([[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thal]])

        # Predict the risk probability
        risk_probability = model.predict_proba(features)[0, 1] * 100

        return render_template('result.html', risk=round(risk_probability, 2))
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
