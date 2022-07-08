from django.contrib import admin
from .models import Student, CommitteeEvaluation, StudentGrades
from import_export import resources
from import_export.admin import ImportExportMixin, ImportExportModelAdmin
from import_export.fields import Field
# Register your models here.


class StudentResource(resources.ModelResource):
    grades_total = Field(column_name='grades_total')
    evaluation_total = Field(column_name='evaluation_total')

    class Meta:
        model = Student

        fields = ('id', 'name', 'file_no', 'group', 'batch', 'birthplace', 'address', 'birthdate', 'religion',
                        'nationality', 'junior_cert_year', 'junior_cert_total', 'guardian', 'guardian_rel', 'guardian_phone', 'national_id',
                        'grades_total', 'evaluation_total')

        export_order = ('id', 'name', 'file_no', 'group', 'batch', 'birthplace', 'address', 'birthdate', 'religion',
                        'nationality', 'junior_cert_year', 'junior_cert_total', 'guardian', 'guardian_rel', 'guardian_phone', 'national_id',
                        'grades_total', 'evaluation_total')

    def dehydrate_grades_total(self, obj):
        total = str(round(obj.student_grades.total / 50 * 100)) + '%'
        return str(obj.student_grades.total)

    def dehydrate_evaluation_total(self, obj):
        total = str(round(obj.committee_eval.total / 50 * 100)) + '%'
        return str(obj.committee_eval.total)


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
    resource_class = StudentResource


admin.site.register(Student, StudentAdmin)
