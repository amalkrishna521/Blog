from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from .forms import signUpForms,EditProfileForm



class UserRegisterView(generic.CreateView):
    form_class=signUpForms
    template_name='registration/registration.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class=EditProfileForm
    template_name='registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

