import pandas as pd
import joblib
from flask import Flask, jsonify, request

app = Flask(__name__)

# http://127.0.0.1:8080/?ret=5&r7=5&r30=5&reth=5&rbnb=5&rada=5&rlt=5

@app.route('/', methods=['GET'])
def predict():
    print('Oui')
    json_ = {'Return': [request.args.get("ret")],
            'Return-7': [request.args.get("r7")],
            'Return-30': [request.args.get("r30")],
            'Return_eth': [request.args.get("reth")],
            'Return_bnb': [request.args.get("rbnb")],
            'Return_ada': [request.args.get("rada")],
            'Return_lite': [request.args.get("rlt")],
      }
    query_df = pd.DataFrame(data=json_)
    print(query_df)
    
    classifier = joblib.load('classifier.pkl')
    prediction = classifier.predict(query_df)
    return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
    app.run(port=8080, debug=False)
    #predict()