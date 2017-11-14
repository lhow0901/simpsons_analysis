import flask
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import operator
import pickle
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier

#---------- MODEL IN MEMORY ----------------#

# Load random forest model and base example to predict an episode's IMBD rating

PREDICTOR = pickle.load(open('models/simpsons.pkl', 'rb'))
base_example = pickle.load(open('models/example.txt', 'rb'))



#---------- URLS AND WEB PAGES -------------#

# Initialize the app
app = flask.Flask(__name__)

# Homepage
@app.route("/")
def viz_page():
    """
    Homepage: serve our visualization page, SimpsonPredictor.html
    """
    with open("SimpsonPredictor.html", 'r') as viz_file:
        return viz_file.read()

# Get an example and return it's score from the predictor model
@app.route("/score", methods=["POST"])
def score():
    """
    When A POST request with json data is made to this uri,
    Read the example from the json, predict probability and
    send it with a response
    """
    # Get decision score for our example that came with the request
    data = flask.request.json
    example = data["example"]
    counter = 4
    for i in example[4:8]:
        example[counter] = ((i*.38)/sum(example[4:8]))
        counter +=1
    x = example + base_example
    x = np.matrix(x)
    scores = list(PREDICTOR.predict_proba(x)[0])
    # Put the result in a nice dict so we can send it as json
    results = {"low":scores[0], "med":scores[1], "high":scores[2]}
    return flask.jsonify(results)

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
app.run(host='0.0.0.0')
app.run(debug=True)
