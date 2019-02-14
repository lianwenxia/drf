from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^pic_code/(.+)', views.ImgCodeView.as_view()),
    url(r'^msg_code/(?P<phone>.+)/', views.MsgCodeView.as_view()),
    # url(r'^msg_code/(?P<phone>.+)/', views.MsgCodeView.as_view()),
    # url(r'^msg_code/(.+)', views.ImgCodeView.as_view()),
    # url(r'^1234', views.TestView.as_view()),

]