from django.contrib import admin
from .models import Student, CommitteeEvaluation, StudentGrades
from import_export import resources
from import_export.admin import ImportExportMixin, ImportExportModelAdmin
from import_export.fields import Field
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin import SimpleListFilter
from django.db.models import Sum, F
from django.db import models
# Register your models here.


class ResultFilter(SimpleListFilter):

    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'النتيجة'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'result'

    def lookups(self, request, model_admin):
        return (
            ('ناجح', 'ناجح'),
            ('راسب', 'راسب')
        )

    def queryset(self, request, queryset):
        students = queryset.annotate(total=Sum(
            F('student_grades__arabic') +
            F('student_grades__math') +
            F('student_grades__science') +
            F('student_grades__social_studies') +
            F('student_grades__english') +
            F('student_grades__spelling') +
            F('student_grades__computer'),
            output_field=models.FloatField()
        ))
        if self.value() == 'ناجح':
            # If is_paid=True filter is activated
            return students.filter(total__gte=17.5)
        if self.value() == 'راسب':
            # If is_paid=True filter is activated
            return students.filter(total__lt=17.5)


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
    list_display = ('name', 'file_no', 'group', 'birthdate',
                    'address', 'junior_cert_total', 'rel_to', 'get_author')
    list_filter = ('birthplace', ResultFilter, 'rel', 'group')

    def get_author(self, obj):
        return format_html('<a href="{}{}/change/">{}</a>', reverse('admin:custom_account_userprofile_changelist'), obj.author.id, obj.author.username)
    get_author.short_description = 'author'


admin.site.register(Student, StudentAdmin)
