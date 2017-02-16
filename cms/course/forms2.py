from django import forms
from django.forms.widgets import DateTimeBaseInput

from course.models import Course


class DateInput(DateTimeBaseInput):
    format_key = 'DATE_INPUT_FORMATS'
    input_type = 'date'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'descreption', 'start_date', 'end_date']
        labels = {
            'name': 'Course name:',
            'descreption': 'Descreption:',
            'start_date': 'Start date:',
            'end_date': 'End date:'
        }
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }


# class EditForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = ['descreption', 'start_date', 'end_date']
#         labels = {
#             'descreption': 'Descreption:',
#             'start_date': 'Start date:',
#             'end_date': 'End date:'
#         }
#         widgets = {
#             'start_date': DateInput(),
#             'end_date': DateInput()
#         }
