from django.conf.urls import url
from sites import views

urlpatterns=[
    url(r'^registration$', views.registration),
    url(r'^login$', views.logIn),
    url(r'^logout$', views.logoutUser),
    url(r'^dashboard$', views.dashboard)
]