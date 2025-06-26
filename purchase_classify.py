from flask import Flask, request
import pickle
import sklearn

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World V2 !</p>"


@app.route("/ping")
def pinger():
    return {"MESSAGE": "Hi I am pinging V2...."}

model_pickle= open("articrafts/model.pkl", 'rb')
clf = pickle.load(model_pickle)

@app.route("/predict", methods=['POST'])
def predict():
    purchase_req = request.get_json()

    if purchase_req['Gender'] == "Male":
        gender = 0
    else:
        gender = 1


    income = purchase_req['Income']
    age = purchase_req['Age']
    
    input_data = [[gender, income, age]]
    prediction = clf.predict(input_data)

    if prediction == 1:
        pred = "yes"
    else:
        pred = "no"

    return {"purchased_status": pred}

#python -m venv sindhuvenv
#source sindhuvenv/bin/activate
#pip install -r requirements.txt
#sindhuvenv\Scripts\activate.bat
#flask app --purchase_classify.py run
