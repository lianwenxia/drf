from django.conf.urls import url, include
from django.contrib import admin
from . import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    url(r'^submit/', views.UserView.as_view()),
    url(r'^userinfo/', views.UserInfoView.as_view()),
    url(r'^change/', views.ChangeView.as_view()),
    # url(r'^test/', views.TestView.as_view()),
    # url(r'^login/', views.LoginView.as_view()),
    url(r'^login/', obtain_jwt_token),
    url(r'^active/(.+)', views.ActiveView.as_view()),

]