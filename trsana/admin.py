from django.contrib import admin
from .models import Student, CommitteeEvaluation, StudentGrades
from import_export import resources
from import_export.admin import ImportExportMixin, ImportExportModelAdmin
# Register your models here.


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student


class CommitteeEvaluationResource(resources.ModelResource):
    class Meta:
        model = CommitteeEvaluation


class StudentGradesResource(resources.ModelResource):
    class Meta:
        model = StudentGrades


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
