from django import forms
from .models import Birthplace, Religion, Student, StudentGrades, CommitteeEvaluation


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(label='اسم الطالب', widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), max_length=50, required=True)
        self.fields['file_no'] = forms.CharField(label='رقم الملف', widget=forms.NumberInput(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), max_length=10, required=True)
        self.fields['group'] = forms.CharField(label='المجموعة', widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), max_length=50, required=True)
        self.fields['batch'] = forms.CharField(label='الدفعة', widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), max_length=50, required=True)
        self.fields['birthdate'] = forms.DateField(
            label='تاريخ الميلاد', widget=forms.DateInput(attrs={'class': 'form-control', 'style': 'width:500px;'}), required=True)
        self.fields['religion'] = forms.ChoiceField(label='الديانة', widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), choices=Religion.choices, required=True)
        self.fields['birthplace'] = forms.ChoiceField(label='محل الميلاد', widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), choices=Birthplace.choices, required=True)
        self.fields['address'] = forms.CharField(label='العنوان', widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), max_length=50, required=True)
        self.fields['nationality'] = forms.CharField(label='الجنسية', widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), max_length=50, required=True)
        self.fields['junior_cert_year'] = forms.CharField(label='سنة اتمام الشهادة الاعدادية', widget=forms.NumberInput(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), max_length=50, required=True)
        self.fields['junior_cert_total'] = forms.FloatField(label='مجموع الشهادة الاعدادية', widget=forms.NumberInput(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), required=True)
        self.fields['junior_cert_place'] = forms.ChoiceField(label='جهة صدور الشهادة الاعدادية', widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), required=True, choices=Birthplace.choices)
        self.fields['guardian'] = forms.CharField(label='اسم ولي الامر', widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), max_length=50, required=True)
        self.fields['guardian_rel'] = forms.CharField(label='صلة قرابة ولي الامر', widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), max_length=50, required=True)
        self.fields['guardian_phone'] = forms.CharField(label='رقم هاتف ولي الامر', widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), max_length=50, required=True)
        self.fields['national_id'] = forms.CharField(label='الرقم القومي', widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:500px;'}), max_length=50, required=True)
        self.fields['student_pic'] = forms.ImageField(
            label='صورة الطالب', widget=forms.FileInput(attrs={'class': 'form-control', 'style': 'width:500px;'}), required=True)
        self.fields['rel'] = forms.BooleanField(label='تابع', widget=forms.CheckboxInput(
            attrs={'class': 'form-control d-block', 'id': 'relChk'}), required=False)
        self.fields['rel_to'] = forms.CharField(label='تابع لـ', widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width:500px;', 'id': 'relName', 'disabled': True}), max_length=50, required=False)
        self.fields['not_attend'] = forms.BooleanField(label='لم يحضر', widget=forms.CheckboxInput(
            attrs={'class': 'form-control', 'id': 'attendChk'}), required=False)

    class Meta:
        model = Student
        fields = '__all__'
        exclude = ('author',)


class CommitteeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommitteeForm, self).__init__(*args, **kwargs)
        self.fields['committee_chairman'] = forms.FloatField(
            label='تقييم رئيس اللجنة', widget=forms.NumberInput(attrs={'class': 'form-control grade', 'style': 'width:500px;'}), required=True)
        self.fields['first_member'] = forms.FloatField(
            label='تقييم العضو الاول', widget=forms.NumberInput(attrs={'class': 'form-control grade', 'style': 'width:500px;'}), required=True)
        self.fields['second_member'] = forms.FloatField(
            label='تقييم العضو الثاني', widget=forms.NumberInput(attrs={'class': 'form-control grade', 'style': 'width:500px;'}), required=True)
        self.fields['third_member'] = forms.FloatField(
            label='تقييم العضو الثالث', widget=forms.NumberInput(attrs={'class': 'form-control grade', 'style': 'width:500px;'}), required=True)
        self.fields['forth_member'] = forms.FloatField(
            label='تقييم العضو الرابع', widget=forms.NumberInput(attrs={'class': 'form-control grade', 'style': 'width:500px;'}), required=True)

    class Meta:
        model = CommitteeEvaluation
        fields = ['committee_chairman', 'first_member',
                  'second_member', 'third_member', 'forth_member']


class StudentGradesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentGradesForm, self).__init__(*args, **kwargs)
        self.fields['arabic'] = forms.FloatField(
            label='درجة اللغة العربية', widget=forms.NumberInput(attrs={'class': 'form-control grade', 'style': 'width:500px;'}), required=True)
        self.fields['english'] = forms.FloatField(
            label='درجة اللغة الانجليزية', widget=forms.NumberInput(attrs={'class': 'form-control grade', 'style': 'width:500px;'}), required=True)
        self.fields['math'] = forms.FloatField(label='درجة الرياضيات', widget=forms.NumberInput(
            attrs={'class': 'form-control grade', 'style': 'width:500px;'}), required=True)
        self.fields['science'] = forms.FloatField(
            label='درجة العلوم', widget=forms.NumberInput(attrs={'class': 'form-control grade', 'style': 'width:500px;'}), required=True)
        self.fields['social_studies'] = forms.FloatField(
            label='درجة الدراسات الاجتماعية', widget=forms.NumberInput(attrs={'class': 'form-control grade', 'style': 'width:500px;'}), required=True)
        self.fields['computer'] = forms.FloatField(
            label='درجة الحاسب الالي', widget=forms.NumberInput(attrs={'class': 'form-control grade', 'style': 'width:500px;'}), required=True)
        self.fields['spelling'] = forms.FloatField(
            label='درجة الاملاء', widget=forms.NumberInput(attrs={'class': 'form-control grade', 'style': 'width:500px;'}), required=True)

    class Meta:
        model = StudentGrades
        fields = ['arabic', 'math', 'science',
                  'social_studies', 'computer', 'english', 'spelling']
