from flask import Flask, render_template,request

import pickle

app=Flask(__name__)

#load model
model =pickle.load(open('irismodel.sav','rb'))

@app.route("/")
def home():
    return render_template('index.html',result="")

@app.route('/predict',methods=['POST','GET'])
@app.route('/predict', methods=['POST'])
def predict():
    try:
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        return render_template('index.html', result=prediction[0])
    except:
        return render_template('index.html', result="Invalid Input")

if __name__ =="__main__":
    app.run(debug=True)