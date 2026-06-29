from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import researcher, Capstone, Student, Book, StudentPrediction
from .forms import StudentForm, BookForm, PredictionForm
import pandas as pd
import joblib
import os
from django.conf import settings
from .models import PredictionHistory
from .models import StudentPrediction, PredictionHistory 
from .forms import PredictionForm, BurnoutPredictionForm
# --- Load ML Model and Features ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(BASE_DIR, "ml", "student_model.pkl"))

# CRITICAL: We load the feature columns saved during train.py 
# so Django knows exactly how to format the dummy variables.
model_columns = joblib.load(os.path.join(BASE_DIR, "ml", "model_features.pkl"))

# --- Existing Views ---
def home(request):
    # Fetch all AI predictions instead of capstones, ordered by newest first
    predictions = StudentPrediction.objects.all().order_by('-created_at')
    
    # Pass the predictions to your home.html template
    return render(request, 'home.html', {'predictions': predictions})

def researcherpage(request):
    researchers = researcher.objects.all()
    return render(request, 'researchers.html', {'researchers': researchers})
    
def about(request):
    return render(request, 'about.html')

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')

# --- Book Views ---
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('book_list')


# --- NEW Machine Learning View ---
def predict_student(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)

        if form.is_valid():
            # 1. Put all cleaned form data directly into a Pandas DataFrame
            # This is much cleaner than pulling out 14 variables one by one!
            input_df = pd.DataFrame([form.cleaned_data])

            # 2. Apply One-Hot Encoding just like we did in train.py
            input_encoded = pd.get_dummies(input_df)

            # 3. Align Columns with the ML Model
            # The user only selected one Major (e.g., 'STEM'), but the model is 
            # expecting columns for all majors (STEM, Arts, Business, etc.).
            # reindex() automatically adds the missing columns and fills them with 0s.
            input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

            # 4. Make the Prediction
            result = model.predict(input_encoded)
            prediction_text = "HIGH RISK" if result[0] == 1 else "SAFE"

            # 5. Save the prediction to the database
            # We use **form.cleaned_data to automatically unpack the dictionary 
            # and map it to the database fields, then add the prediction.
            StudentPrediction.objects.create(
                **form.cleaned_data,
                prediction=prediction_text
            )

            # 6. Render the Result page
            return render(request, "result.html", {
                "prediction": prediction_text
            })

    else:
        # GET request: send an empty form
        form = PredictionForm()

    # NOTE: I combined your duplicate predict_view and predict_student into this 
    # single function. Ensure your urls.py maps 'predict/' to views.predict_student
    return render(request, "predict_view.html", {"form": form})

# --- Prediction History View ---
def prediction_list(request):
    # This queries your updated StudentPrediction model for all history logs,
    # sorting them with the newest entries showing at the top (-created_at)
    predictions = StudentPrediction.objects.all().order_by('-created_at')
    
    return render(
        request, 
        'prediction_list.html', 
        {'predictions': predictions}
    )


# I changed 'your_app_name' to 'ml2' based on your previous terminal logs!
MODEL_PATH = os.path.join(settings.BASE_DIR, 'ml2', 'student_burnout_model.pkl')
SCALER_PATH = os.path.join(settings.BASE_DIR, 'ml2', 'student_scaler.pkl')
FEATURES_PATH = os.path.join(settings.BASE_DIR, 'ml2', 'model_features.pkl')

def predict_burnout(request):
    if request.method == 'POST':
        # Bind the POST data to our new form
        form = BurnoutPredictionForm(request.POST)
        
        if form.is_valid():
            try:
                # 1. Use cleaned_data to safely get the user's inputs
                raw_data = form.cleaned_data

                # 2. Convert to Pandas DataFrame
                df_input = pd.DataFrame([raw_data])

                # 3. Apply Feature Engineering
                df_input['Total_Study_Hours'] = df_input['Weekly_GenAI_Hours'] + df_input['Traditional_Study_Hours']

                # Drop the student_name from the DataFrame because the ML model doesn't use it to predict
                df_for_ml = df_input.drop(columns=['student_name'])

                # 4. Perform One-Hot Encoding
                df_encoded = pd.get_dummies(df_for_ml)

                # 5. Load the required columns and align them
                model_features = joblib.load(FEATURES_PATH)
                df_aligned = df_encoded.reindex(columns=model_features, fill_value=0)

                # 6. Load Scaler and Scale the features
                scaler = joblib.load(SCALER_PATH)
                X_scaled = scaler.transform(df_aligned)

                # 7. Load Model and Predict
                model = joblib.load(MODEL_PATH)
                prediction = model.predict(X_scaled)[0]

                result = "High Risk of Burnout" if prediction == 1 else "Safe / Low Risk"

                # 8. Save to Database
                PredictionHistory.objects.create(
                    student_name=raw_data.get('student_name', 'Anonymous'),
                    weekly_genai_hours=raw_data['Weekly_GenAI_Hours'],
                    traditional_study_hours=raw_data['Traditional_Study_Hours'],
                    anxiety_level=raw_data['Anxiety_Level_During_Exams'],
                    prediction_result=result
                )

                # 9. Return the result to the user (CHANGED to result_burnout.html)
                return render(request, 'result_burnout.html', {'result': result, 'data': raw_data})

            except Exception as e:
                # If an error happens, reload the page (CHANGED to predict_burnout.html)
                return render(request, 'predict_burnout.html', {'form': form, 'error': str(e)})

    else:
        # If it's a GET request, just load the empty form
        form = BurnoutPredictionForm()

    # Pass the form to the template (CHANGED to predict_burnout.html)
    return render(request, 'predict_burnout.html', {'form': form})


def prediction_history(request):
    """View to fetch and display past predictions"""
    history = PredictionHistory.objects.all().order_by('-created_at')
    # (CHANGED to history_burnout.html)
    return render(request, 'history_burnout.html', {'history': history})