from django.conf.urls import url

from course import views

urlpatterns = [
    url(r'^$', views.show_courses, name='show_courses'),
    url(r'^new$', views.create_course, name='create_course'),
    url(r'^edit/(?P<course_name>[A-Za-z]+)$', views.edit_course,
        name='edit_course'),
    url(r'(?P<course_name>[A-Za-z0-9]+)$', views.detail_course,
        name='detail_course')
]
