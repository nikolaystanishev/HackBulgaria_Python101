from django.shortcuts import render

from lecture.models import Lecture

from lecture.forms import EditForm
from lecture.forms2 import LectureForm


# Create your views here.
def detail_lecture(request, *args, **kwargs):
    if request.method == 'GET':
        lecture = Lecture.objects.get(id=kwargs['lecture_id'])
    return render(request, 'detail_lecture.html', locals())


def create_lecture(request):
    if request.method == 'POST':
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save()
    form = LectureForm()
    return render(request, 'create_course.html', locals())


def edit_lecture(request, *args, **kwargs):
    lecture_id = kwargs['lecture_id']
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            form.save(lecture_id)
    form = EditForm()
    return render(request, 'edit_lecture.html', locals())
