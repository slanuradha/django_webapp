from django.conf.urls import url
from form_example import views

urlpatterns =[
    url(r'^user_form$', views.user_form),
    url(r'^static_example$', views.static_example)
]