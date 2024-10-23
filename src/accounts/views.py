from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('login')

class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')
    
    
    
    