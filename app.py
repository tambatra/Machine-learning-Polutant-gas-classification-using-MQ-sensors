from my_Model import ML_Model
from flask import Flask, request

app = Flask(__name__)
model = ML_Model()


@app.route('/predict')
def predict():
    Q1 = int(request.args.get('Q1'))
    Q2 = int(request.args.get('Q2'))
    Q3 = int(request.args.get('Q3'))
    Q4 = int(request.args.get('Q4'))
    return str(model.predict(Q1, Q2, Q3, Q4))


if __name__ == "__main__":
    app.run(debug=False)
