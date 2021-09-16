from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)
model=pickle.load(open('Model/model.pickle', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
    #if(request.method == 'GET'):
       #data = 'Hello'
        #return jsonify({'data':data})

@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    pred = model.predict(final_features)
    output = round(pred[0], 2)
    return render_template('index.html', prediction_text ='Housing price prediction: ${}'.format(output))

@app.route('/api/')
def api():
    bedrooms = request.args.get('bedrooms')
    bathrooms = request.args.get('bathrooms')
    sqft = request.args.get('sqft_living')
    floors = request.args.get('floors')
    condition = request.args.get('condition')

    df = pd.DataFrame({'Bedrooms':[bedrooms], 'Bathrooms':[bathrooms], 'SqFt': [sqft], 'Floors':[floors], 'Condition': [condition]})
    df_pred = model.predict(df)

    output =  jsonify({'House Price':str(df_pred)})
        

    return output

if __name__ == "__main__":
    app.run(debug=True)