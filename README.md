# ⚡ Electric Motor PM Temperature Prediction (Flask + ML)

Small Flask app and training scripts for predicting **PM (Permanent Magnet) temperature** from motor sensor inputs using Machine Learning.

---

## 📂 Repository Layout

```
electric_motor_app/
│
├── app.py                     # Flask web application
├── train_model.py             # Simple training script
├── train_model_eval.py        # Training + evaluation version
├── requirements.txt           # Python dependencies
│
├── data/
│   └── motor_data.csv         # Dataset
│
├── model/
│   ├── decision_tree_model.pkl
│   └── scaler.pkl
│
├── templates/
│   ├── Manual_predict.html
│   └── Sensor_predict.html
```

---

## ⚙️ Setup

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧠 Training

### 🔹 Quick Training (Simple Pipeline)

Run:

```bash
python train_model.py
```

This script:

* Loads `motor_data.csv`
* Uses features:

  * `ambient`
  * `coolant`
  * `u_d`
  * `u_q`
  * `motor_speed`
  * `i_d`
  * `i_q`
  * `stator_yoke`
  * `stator_winding`
* Target: `pm`
* Scales features using `MinMaxScaler`
* Trains `DecisionTreeRegressor`
* Saves:

  * `model/decision_tree_model.pkl`
  * `model/scaler.pkl`

---

### 🔹 Detailed Training (With Evaluation)

Run:

```bash
python train_model_eval.py
```

This script:

* Drops extra columns if present
* Trains with:

  * `max_depth`
  * `min_samples_leaf`
* Prints:

  * **RMSE**
  * **R² Score**
* Saves model and scaler to `model/` folder

> 💡 Tip: Keep **only one training script** or make sure both save to the same `model/` directory.

---

## 🚀 Running the Web App

Start the server:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🌐 Flask Routes

| Route      | Method | Description                   |
| ---------- | ------ | ----------------------------- |
| `/`        | GET    | Manual input page             |
| `/predict` | POST   | Predict PM temperature        |
| `/sensor`  | GET    | Sensor-based UI (placeholder) |

---

## 📝 Manual Form Fields (Order Matters!)

Your model **expects inputs in this exact order**:

1. ambient
2. coolant
3. u_d
4. u_q
5. motor_speed
6. i_d
7. i_q
8. stator_yoke
9. stator_winding

⚠️ The order **must match** training and `app.py` feature list.

---

## 📌 Prediction Notes

* `app.py` loads:

  * `decision_tree_model.pkl`
  * `scaler.pkl`
* Inputs are **scaled before prediction**.
* Target `pm` is **not scaled**.
* If UI shows “Normalized”, update label if output is actual temperature.

---

## 🛠️ Recommended Improvements

* Unify preprocessing & save paths
* Add input validation & shape checks
* Improve UI with units & limits
* Add tests for model and endpoints
* Use `debug=False` for production
* Add logging & error handling

---

## 🧪 Quick Troubleshooting

| Issue            | Fix                            |
| ---------------- | ------------------------------ |
| Model not found  | Check `model/` folder paths    |
| Feature mismatch | Ensure 9 inputs                |
| NaN predictions  | Print `X.shape` before scaling |
| CSV not found    | Check `data/motor_data.csv`    |
