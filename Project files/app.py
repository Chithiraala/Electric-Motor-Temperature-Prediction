from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("model/decision_tree_model.pkl")
scaler = joblib.load("model/scaler.pkl")

# Must match training order EXACTLY
features = [
    "ambient", "coolant", "u_d", "u_q",
    "motor_speed", "i_d", "i_q",
    "stator_yoke", "stator_winding"
]

@app.route("/")
def home():
    return render_template("Manual_predict.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read inputs in correct order
        values = [float(request.form[f]) for f in features]

        # Convert to 2D array
        X = np.array(values).reshape(1, -1)

        # Scale using SAME scaler as training
        X_scaled = scaler.transform(X)

        # Predict
        prediction = model.predict(X_scaled)[0]

        return render_template(
            "Manual_predict.html",
            result=f"{prediction:.2f}"
        )

    except Exception as e:
        return render_template(
            "Manual_predict.html",
            result=f"Error: {str(e)}"
        )

@app.route("/sensor")
def sensor():
    return render_template("Sensor_predict.html")

if __name__ == "__main__":
    app.run(debug=True)
