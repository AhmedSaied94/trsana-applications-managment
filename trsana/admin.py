from django.contrib import admin
from .models import Student, CommitteeEvaluation, StudentGrades
from import_export import resources
from import_export.admin import ImportExportMixin
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin, ImportExportMixin):
    pass


@admin.register(CommitteeEvaluation)
class CommitteeEvaluationAdmin(admin.ModelAdmin, ImportExportMixin):
    pass


@admin.register(StudentGrades)
class StudentGradesAdmin(admin.ModelAdmin, ImportExportMixin):
    pass


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = '__all__'
