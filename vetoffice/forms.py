from django import forms
from django.db.models import fields
from .models import Owner, Patient


class OwnerCreateForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ("first_name", "last_name", "phone")


class OwnerUpdateForm(forms.ModelForm):
    # Form for updating owner
    class Meta:
        model = Owner
        fields = ("first_name", "last_name", "phone")


class OwnerDeleteForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ("first_name", "last_name", "phone")


class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("pet_name", "animal_type", "breed", "age", "owner")


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("pet_name", "animal_type", "breed", "age", "owner")


class PatientDeleteForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("pet_name", "animal_type", "breed", "age", "owner")
