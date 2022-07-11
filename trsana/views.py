from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import FormView, UpdateView
from requests import request
from .forms import StudentForm, CommitteeForm, StudentGradesForm
from .models import Student, CommitteeEvaluation, StudentGrades
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.


# class AddStudent(FormView):
#     template_name = 'trsana/add_student.html'
#     form_class = StudentForm
#     success_url = '/add-student/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super(UpdateStudent, self).get_context_data(**kwargs)
#         context['url'] = 'add-student'
#         context['title'] = 'اضافة طالب'
#         context['btn'] = 'اضافة الطالب'
#         return context


# class UpdateStudent(UpdateView):
#     template_name = 'trsana/add_student.html'
#     form_class = StudentForm
#     model = Student

#     def get_success_url(self):
#         return reverse('update-student', kwargs={'pk': self.kwargs['pk']})

#     # def get_form(self, form_class=form_class):
#     #     student = Student.objects.get(pk=self.kwargs['pk'])
#     #     return form_class(instance=student)

#     def get_context_data(self, **kwargs):
#         context = super(UpdateStudent, self).get_context_data(**kwargs)
#         context['url'] = self.kwargs['pk']
#         context['title'] = 'تعديل طالب'
#         context['btn'] = 'تحديث الطالب'
#         return context

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.save()
#         return super(UpdateStudent, self).form_valid(form)


@login_required
def add_student(request):
    if not request.user.is_active:
        return render(request, 'trsana/403.html')
    student_form = StudentForm()
    committee_form = CommitteeForm()
    grades_form = StudentGradesForm()
    context = {
        'title': 'طالب جديد',
        'url': 'add-student',
        'btn': 'اضافة طالب',
        'title': 'add'
    }
    if request.method == 'POST':
        student_form = StudentForm(data=request.POST, files=request.FILES)
        committee_form = CommitteeForm(data=request.POST)
        grades_form = StudentGradesForm(data=request.POST)
        print(student_form.errors, student_form.cleaned_data)
        print(committee_form.is_valid())
        print(grades_form.is_valid())
        if student_form.is_valid() and committee_form.is_valid() and grades_form.is_valid():
            print('here')
            student = student_form.save()
            student.author = request.user
            student.save()
            committe_data = committee_form.cleaned_data
            grades_data = grades_form.cleaned_data
            committee_eval = CommitteeEvaluation()
            committee_eval.committee_chairman = committe_data['committee_chairman']
            committee_eval.first_member = committe_data['first_member']
            committee_eval.second_member = committe_data['second_member']
            committee_eval.third_member = committe_data['third_member']
            committee_eval.forth_member = committe_data['forth_member']
            committee_eval.student = student
            committee_eval.save()
            grades = StudentGrades()
            grades.arabic = grades_data['arabic']
            grades.math = grades_data['math']
            grades.science = grades_data['science']
            grades.social_studies = grades_data['social_studies']
            grades.computer = grades_data['computer']
            grades.english = grades_data['english']
            grades.spelling = grades_data['spelling']
            grades.student = student
            grades.save()
            return redirect('student_detail', student.id)
        else:
            context['student_form'] = student_form
            context['committee_form'] = committee_form
            context['grades_form'] = grades_form

            return render(request, 'trsana/add_student.html', context=context)
    else:
        context['student_form'] = student_form
        context['committee_form'] = committee_form
        context['grades_form'] = grades_form
        return render(request, 'trsana/add_student.html', context=context)


@login_required
def update_student(request, pk):
    if not request.user.is_staff:
        return render(request, 'trsana/403.html')
    student = get_object_or_404(Student, pk=pk)
    student_form = StudentForm(instance=student)
    committee_form = CommitteeForm(instance=student.committee_eval)
    grades_form = StudentGradesForm(instance=student.student_grades)
    context = {
        'title': 'تعديل طالب',
        'url': student.id,
        'btn': 'تعديل الطالب',
    }
    if request.method == 'POST':
        student_form = StudentForm(
            data=request.POST, files=request.FILES, instance=student)
        committee_form = CommitteeForm(
            data=request.POST, instance=student.committee_eval)
        grades_form = StudentGradesForm(
            data=request.POST, instance=student.student_grades)
        if student_form.is_valid() and committee_form.is_valid() and grades_form.is_valid():
            student_form.save()
            committee_form.save()
            grades_form.save()
            return redirect('student_detail', student.id)
        else:
            context['student_form'] = student_form
            context['committee_form'] = committee_form
            context['grades_form'] = grades_form
            return render(request, 'trsana/add_student.html', context=context)
    else:
        context['student_form'] = student_form
        context['committee_form'] = committee_form
        context['grades_form'] = grades_form
        return render(request, 'trsana/add_student.html', context=context)


@login_required
def student_detail(request, pk):
    if not request.user.is_staff:
        return render(request, 'trsana/403.html')
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'trsana/student.html', context={'student': student})


@login_required
def results(request):
    if not request.user.is_staff:
        return render(request, 'trsana/403.html')
    students = Student.objects.all()
    cites = [st.birthplace for st in students]
    if request.GET.get('city') and request.GET.get('city') != 'الكل':
        students = students.filter(birthplace=request.GET.get('city'))
    if request.GET.get('rel') and request.GET.get('rel') != 'الكل':
        rel = request.GET.get('rel')
        students = students.filter(rel=True if rel == 'تابع' else False)
    if request.GET.get('group'):
        students = students.filter(group=request.GET.get('group'))
    if request.GET.get('result') and request.GET.get('result') != 'الكل':
        students = [student for student in students if student.student_grades.result
                    == request.GET.get('result')]
    if request.GET.get('sort') and request.GET.get('sort') != 'بدون':
        sort = request.GET.get('sort')
        if type(students) is not list:
            students = [student for student in students]
        if sort == 'الاعلى درجات':
            students.sort(key=lambda x: x.student_grades.total, reverse=True)
        elif sort == 'الاقل درجات':
            students.sort(key=lambda x: x.student_grades.total)
        elif sort == 'ا - ي':
            students.sort(key=lambda x: x.name)
        elif sort == 'ي - ا':
            students.sort(key=lambda x: x.name, reverse=True)
        elif sort == 'رقم الملف':
            students.sort(key=lambda x: x.file_no)

    return render(request, 'trsana/results.html', context={'students': students, 'title': 'results', 'cites': list(set(cites))})


@login_required
def delete_student(request, pk):
    if not request.user.is_staff:
        return render(request, 'trsana/403.html')
    qs = Student.objects.filter(pk=pk)
    if not qs.exists():
        return render(request, 'trsana/404.html')
    student = qs.first()
    student.delete()
    return redirect('students', 'students')


@login_required
def students(request, temp):
    template = 'trsana/students.html' if temp == 'cards' else 'trsana/students_table.html'
    if not request.user.is_staff:
        return render(request, 'trsana/403.html')
    students = Student.objects.all()
    cites = [st.birthplace for st in students]

    if request.GET.get('city') and request.GET.get('city') != 'الكل':
        students = students.filter(birthplace=request.GET.get('city'))
    if request.GET.get('rel') and request.GET.get('rel') != 'الكل':
        rel = request.GET.get('rel')
        students = students.filter(rel=True if rel == 'تابع' else False)
    if request.GET.get('group'):
        students = students.filter(group=request.GET.get('group'))
    if request.GET.get('result') and request.GET.get('result') != 'الكل':
        students = [student for student in students if student.student_grades.result
                    == request.GET.get('result')]

    if request.GET.get('sort') and request.GET.get('sort') != 'بدون':
        sort = request.GET.get('sort')
        if type(students) is not list:
            students = [student for student in students]
        if sort == 'الاعلى درجات':
            students.sort(key=lambda x: x.student_grades.total, reverse=True)
        elif sort == 'الاقل درجات':
            students.sort(key=lambda x: x.student_grades.total)
        elif sort == 'ا - ي':
            students.sort(key=lambda x: x.name)
        elif sort == 'ي - ا':
            students.sort(key=lambda x: x.name, reverse=True)
        elif sort == 'رقم الملف':
            students.sort(key=lambda x: x.file_no)
    if request.GET.get('search') and request.GET.get('search') != '':
        students = students.filter(name__startswith=request.GET.get('search'))

    return render(request, template,
                  context={
                      'students': students,
                      'title': 'students' if temp == 'cards' else 'students_table',
                      'cites': list(set(cites))
                  })


def home(request):
    return render(request, 'trsana/home.html')


def handler404(request, exception):
    response = render(request, 'trsana/404.html')
    response.status_code = 404
    return response


def about(request):
    return render(request, 'trsana/about.html', context={'title': 'about'})
