from django.conf.urls import url

from lecture import views

urlpatterns = [
    url(r'edit/(?P<lecture_id>[0-9]+)$', views.edit_lecture,
        name='edit_lecture'),
    url(r'(?P<lecture_id>[0-9]+)$', views.detail_lecture,
        name='detail_lecture'),
    url(r'new$', views.create_lecture, name='create_lecture')
]
