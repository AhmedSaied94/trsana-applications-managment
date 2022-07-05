from django.contrib import admin
from .models import Student, CommitteeEvaluation, StudentGrades
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(CommitteeEvaluation)
class CommitteeEvaluationAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentGrades)
class StudentGradesAdmin(admin.ModelAdmin):
    pass
