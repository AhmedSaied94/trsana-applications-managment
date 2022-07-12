from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.


class Religion(models.TextChoices):
    مسلم = 'مسلم', 'مسلم'
    مسيحي = 'مسيحي', 'مسيحي'


class Birthplace(models.TextChoices):
    الاسكندرية = 'الاسكندرية', 'الاسكندرية'
    البحيرة = 'البحيرة', 'البحيرة'
    كفرالشيخ = 'كفرالشيخ', 'كفرالشيخ'
    الشرقية = 'الشرقية', 'الشرقية'
    الغربية = 'الغربية', 'الغربية'
    الدقهلية = 'الدقهلية', 'الدقهلية'
    المنوفية = 'المنوفية', 'المنوفية'
    القليوبية = 'القليوبية', 'القليوبية'
    مطروح = 'مطروح', 'مطروح'
    دمياط = 'دمياط', 'دمياط'
    القاهرة = 'القاهرة', 'القاهرة'
    الجيزة = 'الجيزة', 'الجيزة'
    السويس = 'السويس', 'السويس'
    الاسماعيلية = 'الاسماعيلية', 'الاسماعيلية'
    بورسعيد = 'بورسعيد', 'بورسعيد'
    شمالـسيناء = 'شمال سيناء', 'شمال سيناء'
    جنوبـسيناء = 'جنوب سيناء', 'جنوب سيناء'
    الفيوم = 'الفيوم', 'الفيوم'
    المنيا = 'المنيا', 'المنيا'
    اسيوط = 'اسيوط', 'اسيوط'
    بنيـسويف = 'بني سويف', 'بني سويف'
    قنا = 'قنا', 'قنا'
    سوهاج = 'سوهاج', 'سوهاج'
    اسوان = 'اسوان', 'اسوان'
    الاقصر = 'الاقصر', 'الاقصر'
    الواديـالجديد = 'الوادي الجديد', 'الوادي الجديد'
    البحرالاحمر = 'البحرالاحمر', 'البحرالاحمر'


class Student(models.Model):

    name = models.CharField(_("اسم الطالب"), max_length=50)
    file_no = models.IntegerField(_("رقم الملف"), unique=True)
    group = models.CharField(_("المجموعة"), max_length=50)
    batch = models.CharField(_("الدفعة"), max_length=50)
    birthdate = models.DateField(
        _("تاريخ الميلاد"), auto_now=False, auto_now_add=False)
    religion = models.CharField(
        _("الديانة"), max_length=50, choices=Religion.choices, default=Religion.مسلم)
    birthplace = models.CharField(
        _("محل الميلاد"), max_length=50, choices=Birthplace.choices, default=Birthplace.الاسكندرية)
    address = models.CharField(_("العنوان"), max_length=100)
    nationality = models.CharField(_("الجنسية"), max_length=50, default='مصري')
    junior_cert_year = models.CharField(
        _("سنة اتمام الشهادة الاعدادية"), max_length=50)
    junior_cert_total = models.FloatField(_("مجموع الشهادة الاعدادية"))
    junior_cert_place = models.CharField(
        _("جهة صدور الشهادة الاعدادية"), max_length=50, null=True, choices=Birthplace.choices)
    guardian = models.CharField(_("اسم ولي الامر"), max_length=50)
    guardian_rel = models.CharField(_("صلة قرابة ولي الامر"), max_length=50)
    guardian_phone = models.CharField(
        _("رقم هاتف ولي الامر"), max_length=50, unique=True)
    national_id = models.CharField(
        _("الرقم القومي"), max_length=50, unique=True)
    student_pic = models.ImageField(
        _("صورة الطالب"), upload_to='students', unique=True)
    rel = models.BooleanField(_("تابع"), default=False)
    rel_to = models.CharField(
        _("اسم التابع"), max_length=50, null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("المحرر"), on_delete=models.SET_NULL, null=True, related_name='author')

    class Meta:
        verbose_name = _("الطالب")
        verbose_name_plural = _("الطلاب")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse('update-student', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('delete-student', kwargs={'pk': self.pk})


class CommitteeEvaluation(models.Model):
    student = models.OneToOneField(
        "Student", verbose_name=_("الطالب"), on_delete=models.CASCADE, related_name='committee_eval')
    committee_chairman = models.IntegerField(_("رئيس اللجنة"))
    first_member = models.IntegerField(_("العضو الاول"))
    second_member = models.IntegerField(_("العضو الثاني"))
    third_member = models.IntegerField(_("العضو الثالث"))
    forth_member = models.IntegerField(_("العضو الرابع"))

    @property
    def total(self):
        return self.committee_chairman + self.first_member + self.second_member + self.third_member + self.forth_member

    @property
    def result(self):
        if self.total >= 12.5:
            return 'لائق'
        else:
            return 'غير لائق'

    class Meta:
        verbose_name = _("تقييم اللجنة")
        verbose_name_plural = _("تقييمات اللجنة")

    def __str__(self):
        return f'تقييم اللجنة للطالب {self.student.name}'

    def get_absolute_url(self):
        return reverse("CommitteeEvaluation_detail", kwargs={"pk": self.pk})


class StudentGrades(models.Model):

    student = models.OneToOneField("Student", verbose_name=_(
        "درجات الطالب"), related_name='student_grades', on_delete=models.CASCADE)
    arabic = models.IntegerField(_("اللغة العربية"))
    english = models.IntegerField(_("اللغة الانجليزية"))
    math = models.IntegerField(_("الرياضيات"))
    science = models.IntegerField(_("العلوم"))
    social_studies = models.IntegerField(_("الدراسات الاجتماعية"))
    computer = models.IntegerField(_("الحاسب الالي"))
    spelling = models.IntegerField(_("املاء"))

    @property
    def total(self):
        return self.arabic + self.math + self.science + self.social_studies + self.computer + self.english + self.spelling

    @property
    def result(self):
        if self.total >= 17.5:
            return 'ناجح'
        else:
            return 'راسب'

    class Meta:
        verbose_name = _("درجات الطالب")
        verbose_name_plural = _("درجات الطلاب")

    def __str__(self):
        return f'درجات الطالب {self.student.name}'

    def get_absolute_url(self):
        return reverse("StudentGrades_detail", kwargs={"pk": self.pk})
