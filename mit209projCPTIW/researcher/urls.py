from django.urls import path
from . import views

urlpatterns = [
    # --- Main Pages ---
    path('', views.home, name='home'),
    path('researchers/', views.researcherpage, name='researchers'),
    path('about/', views.about, name='about'),

    # --- Student Paths ---
    path('add/', views.add_student, name='add_student'),
    path('list/', views.student_list, name='student_list'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),

    # --- Book Paths ---
    path('add-book/', views.add_book, name='add_book'),
    path('books/', views.book_list, name='book_list'),
    path('edit-book/<int:id>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:id>/', views.delete_book, name='delete_book'),

    # --- NEW: AI Prediction Paths ---
    path("predict/", views.predict_student, name="predict"),
    path('predictions/', views.prediction_list, name='prediction_list'),
]