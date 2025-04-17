from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('', views.landing_page, name="home"),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('signout/', views.signout_view, name='signout'),

    # Password Reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='app_users/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='app_users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='app_users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='app_users/password_reset_complete.html'),
         name='password_reset_complete'),
]
