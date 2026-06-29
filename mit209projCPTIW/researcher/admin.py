from django.contrib import admin
from .models import researcher, Capstone, Student, Book, StudentPrediction

# --- Register standard models safely (Only once!) ---
admin.site.register(researcher)
admin.site.register(Capstone)
admin.site.register(Student)
admin.site.register(Book)

# --- Register the NEW AI Prediction Model with custom styling ---
@admin.register(StudentPrediction)
class StudentPredictionAdmin(admin.ModelAdmin):
    list_display = ('id', 'Major_Category', 'Year_of_Study', 'prediction', 'created_at')
    list_filter = ('prediction', 'Major_Category', 'Year_of_Study')
    search_fields = ('Major_Category', 'prediction')