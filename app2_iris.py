from fastapi import FastAPI
import asyncio
import pickle
from sklearn.tree import DecisionTreeClassifier
import numpy as np

from model.iris_classifier import foo



#initialise the Fast app
application = FastAPI()
clf = foo()

def create():
    with open("./model/iris_classifier.pkl","rb") as f:
        new_clf = pickle.load(f)
    clf = new_clf    
create()
        
# val = create()
    

@application.get("/get_status")
def get():
    return {"training":70,"testing":30}

@application.get("/training")
def training():
    foo()
    create()
    return "training Completed" 

@application.post("/prediction")
async def prediction(payload:dict):
    X_unknown = [payload["sepal-lenght"],payload["sepal-width"],payload["petal-lenght"],payload["petal-width"]]
    X_unknown = np.array(X_unknown).reshape(1,-1)
    prediction = clf.predict(X_unknown)
    return {"predicted_value":prediction[0]}






