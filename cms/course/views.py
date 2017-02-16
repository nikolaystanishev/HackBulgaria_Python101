from django.shortcuts import render

from course.models import Course
from lecture.models import Lecture
from .forms import EditForm
from course.forms2 import CourseForm


# Create your views here.
def show_courses(request):
    if request.method == 'GET':
        courses = Course.objects.all().order_by('start_date')
    return render(request, 'show_courses.html', locals())


def detail_course(request, *args, **kwargs):
    if request.method == 'GET':
        course = Course.objects.get(name=kwargs['course_name'])
        lectures = Lecture.objects.filter(course=course)
    return render(request, 'detail_course.html', locals())


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    form = CourseForm()
    return render(request, 'create_course.html', locals())


def edit_course(request, *args, **kwargs):
    course_name = kwargs['course_name']
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            form.save(course_name)
    form = EditForm()
    return render(request, 'edit_course.html', locals())
