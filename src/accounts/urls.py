from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #loging urls
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('change_password/', views.PasswordChangeView.as_view(), name='change_password'),
    
    #reset passsword
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
