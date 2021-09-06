from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)
model=pickle.load('Model/model.pickle', 'rb')

@app.route('/')
def home():
    return "Insert home here"

@app.route('/predict', methods='POST')
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    pred = model.predict(final_features)

    output = round(pred[0], 2)

    return render_template('index.html', prediction_text =f'Housing price prediction: ${output}')

if __name__ == "__main__":
    app.run(port=5000, debug=True)