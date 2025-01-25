from flask import Flask, request, jsonify
import pickle
from sklearn.tree import DecisionTreeClassifier
import numpy as np

from model.iris_classifier import foo



#initialise the Flask app
app = Flask(__name__)
clf = foo()

def create():
    with open("./model/iris_classifier.pkl","rb") as f:
        new_clf = pickle.load(f)
    clf = new_clf    
create()
        
# val = create()
    

@app.route("/get_status", methods=["GET"])
def get():
    return {"training":70,"testing":30}

@app.route("/training",methods=["GET"])
def training():
    foo()
    create()
    return "training Completed" 

@app.route("/prediction", methods=["POST"])
def prediction():
    payload = request.json
    X_unknown = [payload["sepal-lenght"],payload["sepal-width"],payload["petal-lenght"],payload["petal-width"]]
    X_unknown = np.array(X_unknown).reshape(1,-1)
    prediction = clf.predict(X_unknown)
    return jsonify({"predicted_value":prediction[0]})






if __name__ == "__main__":
    app.run()