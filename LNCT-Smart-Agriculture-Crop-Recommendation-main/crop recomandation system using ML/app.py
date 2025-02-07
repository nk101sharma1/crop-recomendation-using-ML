import numpy as np
from flask import Flask, request, render_template
import pickle

# Create flask app
app = Flask(__name__)

# Load the pre-trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect the form data and convert it to a list of floats
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        
        # Make prediction using the model
        prediction = model.predict(features)
        
        # Return the prediction result to the HTML template
        prediction_text = f"The Recommended Crop is: {prediction[0]}"
        return render_template("index.html", prediction_text=prediction_text)
    
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error in prediction: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
