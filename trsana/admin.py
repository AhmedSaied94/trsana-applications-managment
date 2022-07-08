from django.contrib import admin
from .models import Student, CommitteeEvaluation, StudentGrades
from import_export import resources
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


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = '__all__'
