import numpy as np
import requests
import pickle
from flask import Flask,jsonify,render_template



app =Flask(__name__)
model=pickle.load(open('rfc_tuned_v2.pkl','rb'))


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    float_features=[float(x) for x in requests.form.values()]
    ''' For rendering results on HTML GUI '''
    final_features=[np.array(float_features)]
    prediction=model.predict(final_features)
    output=prediction[0]
    
    return render_template('index.html',prediction_text='It is a ${}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''For Direct API calls through requests'''
    data=requests.get_json(force=True)
    prediction=model.predict([np.array(list(data.values))])

    output=prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)

