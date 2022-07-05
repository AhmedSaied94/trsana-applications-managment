from django.urls import path
from .views import about, home, delete_student, add_student, update_student, student_detail, results, students
urlpatterns = [
    path('add-student/', add_student, name='add-student'),
    path('update-student/<int:pk>/', update_student, name='update-student'),
    path('student-detail/<int:pk>/', student_detail, name='student_detail'),
    path('results/', results, name='results'),
    path('delete-student/<int:pk>/', delete_student, name='delete-student'),
    path('students/', students, name='students'),
    path('', home, name='home'),
    path('about/', about, name='about')
]
