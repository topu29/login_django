from django.conf.urls import url
from login import views

urlpatterns = [
    url('login/', views.login, name='login'),
    url('', views.signup, name='signup'),
]