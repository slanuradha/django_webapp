from django.conf.urls import url
from testapp import views

urlpatterns =[
    url(r'^hello$', views.hello),
    url(r'^hellopython$', views.hellopython),
    url(r'^djangoclass$', views.djangoclass)
]