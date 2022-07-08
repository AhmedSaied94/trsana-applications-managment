from django.contrib import admin
from .models import Student, CommitteeEvaluation, StudentGrades
from import_export import resources
from import_export.admin import ImportExportMixin, ImportExportModelAdmin
# Register your models here.


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = '__all__'


class CommitteeEvaluationResource(resources.ModelResource):
    class Meta:
        model = CommitteeEvaluation
        fields = '__all__'


class StudentGradesResource(resources.ModelResource):
    class Meta:
        model = StudentGrades
        fields = '__all__'


# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin, ImportExportMixin):
#     resource_class = StudentResource


@admin.register(CommitteeEvaluation)
class CommitteeEvaluationAdmin(admin.ModelAdmin, ImportExportMixin):
    resource_class = CommitteeEvaluationResource


@admin.register(StudentGrades)
class StudentGradesAdmin(admin.ModelAdmin, ImportExportMixin):
    resource_class = StudentGradesResource


class StudentAdmin(ImportExportModelAdmin):
    resource_class = Student


admin.site.register(Student, StudentAdmin)
