from django.urls import path, re_path

from . import views



urlpatterns = [
    path(r'', views.index, name='index'),
    re_path('^([0-9]+)/$', views.detail, name='detail'),
    re_path('^register/$', views.RegisterFormView.as_view()),
    re_path('^login/$', views.LoginFormView.as_view()),
    re_path('^logout/$', views.LogoutView.as_view()),
    re_path('^password-change/', views.PasswordChangeView.as_view())
 ]

