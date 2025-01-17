from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from src.redwine.pipeline.prediction import PredictionPipeline  

app = Flask(__name__)  # initializing a flask app

@app.route('/', methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET']) 
def predict():
    if request.method == 'POST':
        try:
            feature_inputs = [
                'fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
                'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
                'pH', 'sulphates', 'alcohol'
            ]
            data = [float(request.form[feature]) for feature in feature_inputs]

            data.append(0.0)  

            data = np.array(data).reshape(1, -1)  
            
            predictor = PredictionPipeline()
            prediction = predictor.predict(data)
            return render_template('result.html', prediction=str(prediction))
        
        except Exception as e:
            print(f'The Exception message is: {e}')
            return render_template('index.html', error=str(e))
    
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)