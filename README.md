# Gender-identity-based-on-tooth-measurement

Project description
Forensic medicine is an interesting area of study. Forensic dentistry is a branch of forensic medicine. During natural calamities or due to some other reasons, many times, it will not be possible to find out the gender of the deceased person. In such cases, certain measurements of the tooth will be taken (as bones and teeth do not decay easily) and gender will be determined.


ML-Model-Flask-Deployment
This is a an ML project done and deployed using Flask API

* Prerequisites
+ Flask=2.3.1
+ numpy=1.24.3
+ pandas=2.0.1
+ requests=2.29.0
+ jinja2=3.1.2
+ scikit-learn=1.2.2
+ pickle

#### Project Structure
* This project has four major parts :

+ ipynb- This folder contains code for our Machine Learning model to predict gender based on the dental metrics . We have two versions of the code.
+ templates - This folder contains the HTML template to allow user to enter dental measurements and it will display the predicted Gender.
+ app.py - This contains Flask APIs that receives dental measures through GUI or API calls, computes the precised value based on our model and returns it.
+ request.py - This uses requests module to call APIs already defined in app.py and displays the returned value.

> Running the project
Ensure that you are in the project home directory. Create the machine learning model by running below command -
`python model.py`
This would create a serialized version of our model into a file model.pkl

Run app.py using below command to start Flask API
`python app.py`
By default, flask will run on port 5000.

Navigate to URL http://localhost:5000
You should be able to view the homepage as below : alt text

Enter valid numerical values in all 3 input boxes and hit Predict.

If everything goes well, you should be able to see the predcited salary vaule on the HTML page! alt text

You can also send direct POST requests to FLask API using Python's inbuilt request module Run the beow command to send the request with some pre-popuated values -
`python request.py`
