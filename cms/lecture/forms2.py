from django import forms

from lecture.models import Lecture


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['name', 'week', 'course', 'url']
        labels = {
            'name': 'Lecture name:',
            'week': 'Week:',
            'course': 'Course name:',
            'url': 'URL:'
        }
