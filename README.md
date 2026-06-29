AI Impact on Students: Academic Performance and Well-being

#Project Goal / Objective

The primary objective of this project is to analyze the impact of Generative AI (GenAI) usage on student academic performance, study habits, and mental well-being. By examining variables such as weekly AI usage, primary use cases, and prompt engineering skills, this project aims to uncover insights into how AI dependency correlates with academic outcomes (GPAs) and psychological factors (anxiety and burnout). Furthermore, the project involves building predictive machine learning models to forecast student performance (Post-Semester GPA) and classify burnout risk levels based on their AI usage and study habits.

Dataset Used

Source: Kaggle - AI Impact on Students Dataset

The dataset contains various attributes related to student demographics, study habits, AI integration, and academic performance. Below is a description of the features used in this project:

Feature Name | Description

| Student_ID | Unique identifier for each student. | | Major_Category | The academic discipline or field of study (e.g., STEM, Business, Humanities). | | Year_of_Study | The student's current academic level (Freshman, Sophomore, Junior, Senior, Graduate). | | Pre_Semester_GPA | The student's Grade Point Average before the semester started. | | Weekly_GenAI_Hours | The number of hours per week the student spends using Generative AI tools. | | Primary_Use_Case | The main purpose for which the student uses AI (e.g., Copywriting/Drafting, Ideation, Debugging). | | Prompt_Engineering_Skill | Self-reported proficiency level in crafting prompts (Beginner, Intermediate, Advanced). | | Tool_Diversity | The number of different AI tools the student utilizes. | | Paid_Subscription | Boolean flag indicating whether the student pays for premium AI services. | | Traditional_Study_Hours | Weekly hours spent studying without the use of AI. | | Perceived_AI_Dependency | Self-reported rating (scale 1-10) of how heavily the student relies on AI. | | Institutional_Policy | The school's stance on AI usage (e.g., Allowed With Citation, Strict Ban). | | Anxiety_Level_During_Exams | Self-reported anxiety levels during examinations (scale 1-10). | | Post_Semester_GPA | The student's Grade Point Average at the end of the semester (Target Variable for Regression). | | Skill_Retention_Score | A metric representing how well the student retained core subject skills. | | Burnout_Risk_Level | Categorical indicator of student burnout risk (Target Variable for Classification). |

Data Cleaning and Preparation Techniques

To ensure high-quality data for exploratory data analysis (EDA) and model training, the following data cleaning and preprocessing steps were applied:

Deduplication: Checking for and dropping duplicated student records to ensure independent observations.
Missing Value Treatment: Imputing or dropping any missing/null values if present in the raw data.
Outlier Detection & Treatment: * 3-Sigma Limit (Standard Deviation) Method: Used to identify statistically extreme values.
Interquartile Range (IQR) Method: Applied to detect outliers in numerical features like Weekly_GenAI_Hours and Post_Semester_GPA.
Outlier Handling: Addressed anomalies using deletion (removing extreme outlier rows) and median imputation (replacing extreme values with the median) to prevent model skewing.
Feature Encoding: Converting categorical features (e.g., Major_Category, Burnout_Risk_Level) into numerical formats using Label Encoding and One-Hot Encoding for machine learning compatibility.
Feature Scaling: Standardizing/Normalizing numerical features to ensure algorithms that rely on distance metrics perform optimally.
Algorithms and Evaluation Metrics

The modeling phase is divided into two parts: Predicting academic outcomes (Regression) and predicting psychological impact (Classification).

Regression Experiments (Predicting Post_Semester_GPA)
Algorithms Used:

Linear Regression (Baseline)
Decision Tree Regressor
Random Forest Regressor
Gradient Boosting (XGBoost / LightGBM)
Evaluation Metrics:

Mean Absolute Error (MAE): To measure the average magnitude of the errors in predictions. Root Mean Squared Error (RMSE): To penalize larger errors and give a sense of variance. R-Squared (
R
2
): To determine the proportion of variance in the final GPA explained by the model's features.

Classification Experiments (Predicting Burnout_Risk_Level)
Algorithms Used:

Logistic Regression (Baseline)
Random Forest Classifier
Support Vector Classifier (SVC)
XGBoost Classifier
Evaluation Metrics:

Accuracy: Overall correctness of the model. Precision & Recall: To evaluate the model's ability to correctly identify high-risk burnout students without false alarms. F1-Score: The harmonic mean of precision and recall, ensuring a balanced evaluation, especially if the target classes are imbalanced. Confusion Matrix: To visually assess true positives vs. false positives across different burnout levels.
