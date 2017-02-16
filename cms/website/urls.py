from django.conf.urls import url

from website import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^profile$', views.profile, name='profile')
]
