from django.db import models

class researcher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    program = models.CharField(max_length=150, help_text="Degree, Course, or Program")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Capstone(models.Model):
    title = models.CharField(max_length=255)
    # Creates a Many-to-One relationship to the Researcher model
    researcher = models.ForeignKey(researcher, on_delete=models.CASCADE, related_name="capstones")
    year_proposed = models.IntegerField(help_text="e.g., 2026")

    def __str__(self):
        # This will display the Capstone title in the Django Admin
        return self.title
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year_published = models.IntegerField()

    def __str__(self):
        return self.title
    

# --- AI Impact on Students Prediction Model ---
class StudentPrediction(models.Model):
    # --- Categorical / Text Features ---
    Major_Category = models.CharField(max_length=50)
    Year_of_Study = models.CharField(max_length=50)
    Primary_Use_Case = models.CharField(max_length=100)
    Prompt_Engineering_Skill = models.CharField(max_length=50)
    Institutional_Policy = models.CharField(max_length=100)
    
    # --- Boolean Feature ---
    Paid_Subscription = models.BooleanField(default=False)

    # --- Numerical / Float Features ---
    Pre_Semester_GPA = models.FloatField()
    Weekly_GenAI_Hours = models.FloatField()
    Traditional_Study_Hours = models.FloatField()
    Post_Semester_GPA = models.FloatField()
    Skill_Retention_Score = models.FloatField()

    # --- Integer Features ---
    Tool_Diversity = models.IntegerField()
    Perceived_AI_Dependency = models.IntegerField()
    Anxiety_Level_During_Exams = models.IntegerField()

    # --- Prediction Result & Timestamp ---
    # Will store strings like "HIGH RISK" or "SAFE"
    prediction = models.CharField(max_length=50) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction: {self.prediction} on {self.created_at.strftime('%Y-%m-%d')}"