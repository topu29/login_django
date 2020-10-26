from django.conf.urls import url
from login import views

urlpatterns = [
    url('login/', views.loginUser, name='loginUser'),
    url('home/', views.homePage,name = 'homePage'),
    url('logout/', views.logoutUser, name='logoutUser'),
    url('user/', views.userPage, name='userPage'),
    url('', views.signup, name='signup'),
]