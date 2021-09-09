from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)
model=pickle.load(open('Model/model.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    pred = model.predict(final_features)

    output = round(pred[0], 2)

    return render_template('index.html', prediction_text ='Housing price prediction: ${}'.format(output))

if __name__ == "__main__":
    app.run(port=5000, debug=True)