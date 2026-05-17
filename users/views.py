from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from . import models, forms
from django.views import generic


class RegisterView(generic.CreateView):
    template_name = 'users/register.html'
    form_class = forms.CustomRegisterForm
    success_url = '/login/'


class LoginView(generic.FormView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm
    success_url = '/user_list/'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('/login/')


class UserListView(generic.ListView):
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all()