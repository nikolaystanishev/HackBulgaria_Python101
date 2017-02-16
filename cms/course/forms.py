from django import forms
from django.forms.widgets import DateTimeBaseInput

from course.models import Course


class DateInput(DateTimeBaseInput):
    format_key = 'DATE_INPUT_FORMATS'
    input_type = 'date'


# class CourseForm(forms.Form):
#     course_name = forms.CharField(max_length=50, label='Course name:')
#     descreption = forms.CharField(max_length=100, label='Descrepton:')
#     start_time = forms.DateField(widget=DateInput, label='Start date:')
#     end_time = forms.DateField(widget=DateInput, label='End date:')

#     def save(self, commit=True):
#         Course.objects.create(name=self.cleaned_data['course_name'],
#                               descreption=self.cleaned_data['descreption'],
#                               start_date=self.cleaned_data['start_time'],
#                               end_date=self.cleaned_data['end_time'])


class EditForm(forms.Form):
    descreption = forms.CharField(max_length=100, label='Descrepton:',
                                  required=False)
    start_time = forms.DateField(widget=DateInput, label='Start date:',
                                 required=False)
    end_time = forms.DateField(widget=DateInput, label='End date:',
                               required=False)

    def save(self, course_name, commit=True):
        course = Course.objects.get(name=course_name)
        if self.cleaned_data['descreption']:
            course.descreption = self.cleaned_data['descreption']
        if self.cleaned_data['start_time']:
            course.start_date = self.cleaned_data['start_time']
        if self.cleaned_data['end_time']:
            course.end_date = self.cleaned_data['end_time']
        course.save()
