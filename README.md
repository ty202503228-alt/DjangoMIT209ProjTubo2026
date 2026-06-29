AI Impact on Students: Academic Performance and Well-being

Project Goal / Objective
The primary objective of this project is to analyze the impact of Generative AI (GenAI) usage on student academic performance, study habits, and mental well-being. By examining variables such as weekly AI usage, primary use cases, and prompt engineering skills, this project aims to uncover insights into how AI dependency correlates with academic outcomes (GPAs) and psychological factors (anxiety and burnout). 

Furthermore, the project involves building predictive machine learning models to forecast student performance (Post-Semester GPA) and classify burnout risk levels based on their AI usage and study habits. The final classification model is deployed via a Django web application.

Dataset Used
**Source:** [Kaggle - AI Impact on Students Dataset](https://www.kaggle.com/) *(Note: Update this link if you have the specific Kaggle URL)*

The dataset contains various attributes related to student demographics, study habits, AI integration, and academic performance. Below is a description of the features used in this project:

| Feature Name | Description |
| :--- | :--- |
| **Student_ID** | Unique identifier for each student (dropped before model training). |
| **Major_Category** | The academic discipline or field of study (e.g., STEM, Business, Humanities). |
| **Year_of_Study** | The student's current academic level (Freshman, Sophomore, Junior, Senior, Graduate). |
| **Pre_Semester_GPA** | The student's Grade Point Average before the semester started. |
| **Weekly_GenAI_Hours** | The number of hours per week the student spends using Generative AI tools. |
| **Primary_Use_Case** | The main purpose for which the student uses AI (e.g., Copywriting, Ideation, Debugging). |
| **Prompt_Engineering_Skill**| Self-reported proficiency level in crafting prompts (Beginner, Intermediate, Advanced). |
| **Tool_Diversity** | The number of different AI tools the student utilizes. |
| **Paid_Subscription** | Boolean flag indicating whether the student pays for premium AI services. |
| **Traditional_Study_Hours** | Weekly hours spent studying without the use of AI. |
| **Perceived_AI_Dependency** | Self-reported rating (scale 1-10) of how heavily the student relies on AI. |
| **Institutional_Policy** | The school's stance on AI usage (e.g., Allowed With Citation, Strict Ban). |
| **Anxiety_Level_During_Exams**| Self-reported anxiety levels during examinations (scale 1-10). |
| **Post_Semester_GPA** | The student's Grade Point Average at the end of the semester *(Target Variable for Regression)*. |
| **Skill_Retention_Score** | A metric representing how well the student retained core subject skills. |
| **Burnout_Risk_Level** | Categorical indicator of student burnout risk *(Target Variable for Classification)*. |
| **Total_Study_Hours** | *(Engineered Feature)* Combined `Weekly_GenAI_Hours` + `Traditional_Study_Hours`. |
| **High_Risk_Flag** | *(Engineered Target)* Binary conversion mapping 'High' burnout to 1, and others to 0. |

Data Cleaning and Preparation Techniques
To ensure high-quality data for exploratory data analysis (EDA) and model training, the following data cleaning and preprocessing steps were applied:

1. **Deduplication:** Checked for and dropped duplicated student records to ensure independent observations.
2. **Missing Value Treatment:** Imputed or dropped any missing/null values if present in the raw data (categorical variables filled with mode, numerical with median).
3. **Outlier Detection & Treatment:** * *3-Sigma Limit (Standard Deviation) Method:* Used to identify statistically extreme values.
   * *Interquartile Range (IQR) Method:* Applied to detect outliers in numerical features like `Weekly_GenAI_Hours` and `Post_Semester_GPA`.
   * *Outlier Handling:* Addressed anomalies using capping (setting upper limits) and median imputation to prevent model skewing.
4. **Feature Encoding:** Converted categorical features (e.g., `Major_Category`, `Burnout_Risk_Level`) into numerical formats using One-Hot Encoding (`pd.get_dummies`) for machine learning compatibility.
5. **Feature Scaling:** Standardized numerical features using `StandardScaler` to ensure algorithms that rely on distance metrics perform optimally.

Algorithms and Evaluation Metrics
The modeling phase is divided into two parts: Predicting academic outcomes (Regression) and predicting psychological impact (Classification).

#Part 1: Regression Experiments (Predicting Post_Semester_GPA)
**Algorithms Used:**
* Linear Regression (Baseline)
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor (XGBoost / LightGBM)

**Evaluation Metrics:**
* **Mean Absolute Error (MAE):** To measure the average magnitude of the errors in predictions.
* **Root Mean Squared Error (RMSE):** To penalize larger errors and give a sense of variance.
* **R-Squared ($R^2$):** To determine the proportion of variance in the final GPA explained by the model's features.

Part 2: Classification Experiments (Predicting Burnout_Risk_Level)
**Algorithms Used:**
* Logistic Regression (Baseline)
* Support Vector Classifier (SVC)
* Random Forest Classifier
* **Gradient Boosting Classifier (Final Selected Model)**

**Evaluation Metrics:**
* **Accuracy:** Overall correctness of the model.
* **Precision & Recall:** To evaluate the model's ability to correctly identify high-risk burnout students without false alarms.
* **F1-Score:** The harmonic mean of precision and recall, ensuring a balanced evaluation (crucial for imbalanced target classes).
* **Confusion Matrix:** To visually assess true positives vs. false positives across different burnout levels.

Web Application Deployment
For the final implementation, the most accurate classification model (**Gradient Boosting**) was integrated into a Django web application. The deployment utilizes three serialized artifacts (included in this repository):
* `student_burnout_model.pkl`: The trained predictive ML engine.
* `student_scaler.pkl`: The fitted StandardScaler to normalize user inputs dynamically.
* `model_features.pkl`: The One-Hot Encoded column schema required to perfectly align web form data with the ML model.
