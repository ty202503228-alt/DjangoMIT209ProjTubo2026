import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# 1. Load Dataset
# Ensure your CSV is in the same folder as this script, or change the path below
df = pd.read_csv("ai_student_impact_dataset (1).csv")

# 2. Data Cleaning
# Remove duplicates
df = df.drop_duplicates()

# Fill missing values (if any exist)
for col in df.columns:
    if df[col].isnull().sum() > 0:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna(df[col].mode()[0])
        else:
            df[col] = df[col].fillna(df[col].median())

# Outlier Treatment (Using IQR on Weekly GenAI Hours to cap extreme values)
Q1 = df['Weekly_GenAI_Hours'].quantile(0.25)
Q3 = df['Weekly_GenAI_Hours'].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + 1.5 * IQR
df.loc[df['Weekly_GenAI_Hours'] > upper_limit, 'Weekly_GenAI_Hours'] = upper_limit


# 3. Feature Engineering & Target Variable (Binary Classification)
# We map 'High' burnout risk to 1 (High Risk) and 'Low'/'Medium' to 0 (Safe).
df["Is_High_Risk"] = (df["Burnout_Risk_Level"] == 'High').astype(int)

# Create new custom feature requested in project requirements
df['Total_Study_Hours'] = df['Weekly_GenAI_Hours'] + df['Traditional_Study_Hours']

# We drop Student_ID, the old Burnout_Risk_Level, and our target variable 
X = df.drop(columns=["Student_ID", "Burnout_Risk_Level", "Is_High_Risk"])
y = df["Is_High_Risk"]


# 4. Process Categorical Data (One-Hot Encoding)
# Converts text columns (like 'STEM' or 'Freshman') into 1s and 0s automatically.
X_encoded = pd.get_dummies(X, drop_first=True)


# 5. Feature Scaling (Version 3 Dataset requirement)
# Standardizes the data so features with larger numbers don't overpower smaller ones.
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_encoded), columns=X_encoded.columns)


# 6. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)


# 7. Create the Model
# Gradient Boosting performs the best for this dataset, exceeding the 80% accuracy requirement.
model = GradientBoostingClassifier(n_estimators=100, random_state=42)


# 8. Train the Model
model.fit(X_train, y_train)


# 9. Evaluate Accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.4f} ({(accuracy * 100):.2f}%)")


# 10. Save the Model, Scaler, and Features for Django Deployment
# Save the model
joblib.dump(model, "student_burnout_model.pkl")

# Save the scaler (Django needs to scale the web form inputs exactly the same way)
joblib.dump(scaler, "student_scaler.pkl")

# Save the feature column names (Django needs this to format the user's form data correctly)
joblib.dump(list(X_scaled.columns), "model_features.pkl")

print("\nSuccess! Saved 'student_burnout_model.pkl', 'student_scaler.pkl', and 'model_features.pkl'.")