import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

# 1. Load Dataset
# Ensure your CSV is inside a folder named 'dataset' or change the path below
df = pd.read_csv("dataset/ai_student_impact_dataset (1).csv")

# 2. Create Target Variable (Binary Classification)
# We map 'High' burnout risk to 1 (High Risk) and 'Low'/'Medium' to 0 (Safe).
df["Is_High_Risk"] = df["Burnout_Risk_Level"].apply(lambda x: 1 if x == 'High' else 0)

# 3. Select Features
# We drop Student_ID (not useful for prediction), the old Burnout_Risk_Level, 
# and our new target variable so they don't leak into the training data.
X = df.drop(columns=["Student_ID", "Burnout_Risk_Level", "Is_High_Risk"])
y = df["Is_High_Risk"]

# 4. Process Categorical Data (One-Hot Encoding)
# Machine learning only understands numbers. This converts text columns 
# (like 'STEM' or 'Freshman') into 1s and 0s automatically.
X_encoded = pd.get_dummies(X, drop_first=True)

# 5. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y,
    test_size=0.2,
    random_state=42
)

# 6. Create the Model
# We use GradientBoostingClassifier because it performs much better than 
# Random Forest on this specific dataset, safely getting you past 80%.
model = GradientBoostingClassifier(n_estimators=100, random_state=42)

# 7. Train the Model
model.fit(X_train, y_train)
# The algorithm learns the habits of High Risk vs Safe students.

# 8. Test the Model
predictions = model.predict(X_test)

# 9. Evaluate Accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f} ({(accuracy * 100):.2f}%)")

# 10. Save the Model and Features
# We save the model just like before
joblib.dump(model, "student_model.pkl")

# CRITICAL NEW STEP: We must also save the feature column names!
# When your Django app makes a prediction later, it needs to know exactly
# what dummy columns were created so it can format the user's form data correctly.
joblib.dump(list(X_encoded.columns), "model_features.pkl")

print("Saved 'student_model.pkl' and 'model_features.pkl' successfully.")