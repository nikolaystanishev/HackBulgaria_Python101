from django import forms

from lecture.models import Lecture


# class LectureForm(forms.Form):
#     lecture_name = forms.CharField(max_length=50, label='Lecture name:')
#     week = forms.CharField(max_length=3, label='Week:')
#     course_name = forms.CharField(max_length=50, label='Course name:')
#     url = forms.URLField(label='Url:')


class EditForm(forms.Form):
    week = forms.CharField(max_length=3, label='Week:', required=False)
    url = forms.URLField(label='Url:', required=False)

    def save(self, lecture_id, commit=True):
        lecture = Lecture.objects.get(id=lecture_id)
        if self.cleaned_data['week']:
            lecture.week = self.cleaned_data['week']
        if self.cleaned_data['url']:
            lecture.url = self.cleaned_data['url']
        lecture.save()
