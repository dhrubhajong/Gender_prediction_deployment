import numpy as np
import requests
from flask import request
import pickle
from flask import Flask,jsonify,render_template



app =Flask(__name__)
model=pickle.load(open('rfc_tuned_v2.pkl','rb'))


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    float_features=[float(x) for x in request.form.values()]
    ''' For rendering results on HTML GUI '''
    final_features=[np.array(float_features)]
    prediction=model.predict(final_features)

    # Convert the prediction to a string
    if prediction[0] == 1:
        output = 'Male'
    else:
        output = 'Female'
    
    return render_template('index.html',prediction_text='The predicted Gender is {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''For Direct API calls through requests'''
    data=requests.get_json(force=True)
    prediction=model.predict([np.array(list(data.values))])

    output=prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)

