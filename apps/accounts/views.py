
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from .forms import CustomUserCreationForm, CustomAuthenticationForm

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class LoginView(SuccessMessageMixin, DjangoLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    success_message = "Successfully logged in!"

    def form_valid(self, form):
        # Default behavior handles login
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("core:home") # Ensure redirect to home

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("core:home")
    success_message = "Account created successfully! You are now logged in."

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # Add message manually since we are overriding form_valid and might bypass mixin's message logic if not careful,
        # but SuccessMessageMixin hooks into form_valid. Let's rely on mixin but we need to call super() or return redirect with message.
        # Actually, standard CreateView + SuccessMessageMixin works best if we let super handle it, but we need to login.
        # So manual message is safer here.
        messages.success(self.request, self.success_message)
        return redirect(self.success_url)

class LogoutView(View):
    def post(self, request):
        logout(request)
        messages.success(request, "Successfully logged out!")
        return redirect("/")
