from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Owner, Patient
from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, PatientUpdateForm


# Create your views here.

def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def home(request):
    context = {"name": request.user}
    return render(request, 'vetoffice/home.html', context)


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class OwnerList(LoginRequiredMixin, ListView):
    model = Owner


class OwnerCreate(LoginRequiredMixin, CreateView):
    model = Owner
    template_name = 'vetoffice/owner_create_form.html'
    form_class = OwnerCreateForm


class OwnerUpdate(LoginRequiredMixin, UpdateView):
    model = Owner
    template_name = "vetoffice/owner_update_form.html"
    form_class = OwnerUpdateForm


class OwenerDelete(LoginRequiredMixin, DeleteView):
    model = Owner
    template_name = "vetoffice/owner_delete_form.html"
    success_url = "/owner/list"


class PatientList(LoginRequiredMixin, ListView):
    model = Patient


class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = "vetoffice/patient_create_form.html"
    form_class = PatientCreateForm


class PatientUpdate(LoginRequiredMixin, UpdateView):
    model = Patient
    template_name = "vetoffice/patient_update_form.html"
    form_class = PatientUpdateForm


class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = "vetoffice/patient_delete_form.html"
    success_url = "/patient/list"
