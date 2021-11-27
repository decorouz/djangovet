from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Owner, Patient
from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, PatientUpdateForm


# Create your views here.


def home(request):
    context = {"name": "Adeyemi"}
    return render(request, 'vetoffice/home.html', context)


class OwnerList(ListView):
    model = Owner


class OwnerCreate(CreateView):
    model = Owner
    template_name = 'vetoffice/owner_create_form.html'
    form_class = OwnerCreateForm


class OwnerUpdate(UpdateView):
    model = Owner
    template_name = "vetoffice/owner_update_form.html"
    form_class = OwnerUpdateForm


class OwenerDelete(DeleteView):
    model = Owner
    template_name = "vetoffice/owner_delete_form.html"
    success_url = "/owner/list"


class PatientList(ListView):
    model = Patient


class PatientCreate(CreateView):
    models = Patient
    template_name = "vetoffice/patient_create_form.html"
    form_class = PatientCreateForm


class PatientUpdate(UpdateView):
    models = Patient
    template_name = "vetoffice/patient_update_form.html"
    form_class = PatientUpdateForm


class PatientDelete(DeleteView):
    models = Patient
    template_name = "vetoffice/patient_delete_form.html"
    success_url = "/patient/list"