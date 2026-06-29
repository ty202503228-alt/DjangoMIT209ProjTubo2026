from django import forms
from .models import Student
from .models import Book

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


# --- EXISTING AI STUDENT IMPACT PREDICTION FORM ---
class PredictionForm(forms.Form):
    # --- Dropdown Menus (Categorical Data) ---
    MAJOR_CHOICES = [
        ('STEM', 'STEM'), 
        ('Business', 'Business'), 
        ('Humanities', 'Humanities'), 
        ('Medical', 'Medical'), 
        ('Arts', 'Arts')
    ]
    YEAR_CHOICES = [
        ('Freshman', 'Freshman'), 
        ('Sophomore', 'Sophomore'), 
        ('Junior', 'Junior'), 
        ('Senior', 'Senior'), 
        ('Graduate', 'Graduate')
    ]
    USE_CASE_CHOICES = [
        ('Copywriting/Drafting', 'Copywriting/Drafting'), 
        ('Summarizing_Reading', 'Summarizing/Reading'), 
        ('Debugging/Troubleshooting', 'Debugging/Troubleshooting'), 
        ('Ideation', 'Ideation'), 
        ('Direct Answer Generation', 'Direct Answer Generation')
    ]
    SKILL_CHOICES = [
        ('Beginner', 'Beginner'), 
        ('Intermediate', 'Intermediate'), 
        ('Advanced', 'Advanced')
    ]
    POLICY_CHOICES = [
        ('Allowed_With_Citation', 'Allowed With Citation'), 
        ('Strict_Ban', 'Strict Ban'), 
        ('Actively_Encouraged', 'Actively Encouraged')
    ]

    Major_Category = forms.ChoiceField(choices=MAJOR_CHOICES, label="Major Category")
    Year_of_Study = forms.ChoiceField(choices=YEAR_CHOICES, label="Year of Study")
    Primary_Use_Case = forms.ChoiceField(choices=USE_CASE_CHOICES, label="Primary AI Use Case")
    Prompt_Engineering_Skill = forms.ChoiceField(choices=SKILL_CHOICES, label="Prompt Engineering Skill")
    Institutional_Policy = forms.ChoiceField(choices=POLICY_CHOICES, label="School AI Policy")
    
    # --- Checkbox (Boolean) ---
    Paid_Subscription = forms.BooleanField(required=False, label="Do you pay for Premium AI (e.g., ChatGPT Plus)?")

    # --- Number Inputs ---
    Pre_Semester_GPA = forms.FloatField(min_value=1.0, max_value=4.0, label="Pre-Semester GPA (1.0 - 4.0)")
    Post_Semester_GPA = forms.FloatField(min_value=1.0, max_value=4.0, label="Post-Semester GPA (1.0 - 4.0)")
    Weekly_GenAI_Hours = forms.FloatField(min_value=0, label="Weekly GenAI Hours")
    Traditional_Study_Hours = forms.FloatField(min_value=0, label="Weekly Traditional Study Hours")
    Skill_Retention_Score = forms.FloatField(min_value=0, max_value=100, label="Skill Retention Score (0 - 100)")

    # --- Sliders / Scales (Integers) ---
    Tool_Diversity = forms.IntegerField(min_value=1, max_value=5, label="Number of AI Tools Used (1-5)")
    Perceived_AI_Dependency = forms.IntegerField(min_value=1, max_value=10, label="How dependent are you on AI? (1-10)")
    Anxiety_Level_During_Exams = forms.IntegerField(min_value=1, max_value=10, label="Exam Anxiety Level (1-10)")


# --- NEW BURNOUT PREDICTION FORM (Final Project) ---
class BurnoutPredictionForm(forms.Form):
    # Added a name field so the history database can record who the prediction was for
    student_name = forms.CharField(max_length=100, required=False, label="Student Name (Optional)", initial="Anonymous")

    # --- Dropdown Menus (Categorical Data) ---
    MAJOR_CHOICES = [
        ('STEM', 'STEM'), 
        ('Business', 'Business'), 
        ('Humanities', 'Humanities'), 
        ('Medical', 'Medical'), 
        ('Arts', 'Arts')
    ]
    YEAR_CHOICES = [
        ('Freshman', 'Freshman'), 
        ('Sophomore', 'Sophomore'), 
        ('Junior', 'Junior'), 
        ('Senior', 'Senior'), 
        ('Graduate', 'Graduate')
    ]
    USE_CASE_CHOICES = [
        ('Copywriting/Drafting', 'Copywriting/Drafting'), 
        ('Summarizing_Reading', 'Summarizing/Reading'), 
        ('Debugging/Troubleshooting', 'Debugging/Troubleshooting'), 
        ('Ideation', 'Ideation'), 
        ('Direct Answer Generation', 'Direct Answer Generation')
    ]
    SKILL_CHOICES = [
        ('Beginner', 'Beginner'), 
        ('Intermediate', 'Intermediate'), 
        ('Advanced', 'Advanced')
    ]
    POLICY_CHOICES = [
        ('Allowed_With_Citation', 'Allowed With Citation'), 
        ('Strict_Ban', 'Strict Ban'), 
        ('Actively_Encouraged', 'Actively Encouraged')
    ]

    Major_Category = forms.ChoiceField(choices=MAJOR_CHOICES, label="Major Category")
    Year_of_Study = forms.ChoiceField(choices=YEAR_CHOICES, label="Year of Study")
    Primary_Use_Case = forms.ChoiceField(choices=USE_CASE_CHOICES, label="Primary AI Use Case")
    Prompt_Engineering_Skill = forms.ChoiceField(choices=SKILL_CHOICES, label="Prompt Engineering Skill")
    Institutional_Policy = forms.ChoiceField(choices=POLICY_CHOICES, label="School AI Policy")
    
    # --- Checkbox (Boolean) ---
    Paid_Subscription = forms.BooleanField(required=False, label="Do you pay for Premium AI (e.g., ChatGPT Plus)?")

    # --- Number Inputs ---
    Pre_Semester_GPA = forms.FloatField(min_value=1.0, max_value=4.0, label="Pre-Semester GPA (1.0 - 4.0)")
    Post_Semester_GPA = forms.FloatField(min_value=1.0, max_value=4.0, label="Post-Semester GPA (1.0 - 4.0)")
    Weekly_GenAI_Hours = forms.FloatField(min_value=0, label="Weekly GenAI Hours")
    Traditional_Study_Hours = forms.FloatField(min_value=0, label="Weekly Traditional Study Hours")
    Skill_Retention_Score = forms.FloatField(min_value=0, max_value=100, label="Skill Retention Score (0 - 100)")

    # --- Sliders / Scales (Integers) ---
    Tool_Diversity = forms.IntegerField(min_value=1, max_value=5, label="Number of AI Tools Used (1-5)")
    Perceived_AI_Dependency = forms.IntegerField(min_value=1, max_value=10, label="How dependent are you on AI? (1-10)")
    Anxiety_Level_During_Exams = forms.IntegerField(min_value=1, max_value=10, label="Exam Anxiety Level (1-10)")