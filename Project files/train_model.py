import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("data/motor_data.csv")

X = df[['ambient','coolant','u_d','u_q','motor_speed','i_d','i_q','stator_yoke','stator_winding']]
y = df['pm']

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = DecisionTreeRegressor()
model.fit(X_train, y_train)

joblib.dump(model, "model/decision_tree_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("Model and Scaler saved successfully!")
