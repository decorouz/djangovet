from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("owner/list", views.OwnerList.as_view(), name="ownerlist"),
    path("owner/create", views.OwnerCreate.as_view(), name="ownercreate"),
    path("owner/update/<pk>", views.OwnerUpdate.as_view(), name="ownerupdate"),
    path("owner/delete/<pk>", views.OwenerDelete.as_view(), name="ownerdelete"),
    path("patient/list", views.PatientList.as_view(), name="patientlist"),
    path("patient/create", views.PatientCreate.as_view(), name="patientcreate"),
    path("patient/update/<pk>", views.PatientUpdate.as_view(), name="patientupdate"),
    path("patient/delete/<pk>", views.PatientDelete.as_view(), name="patientdelete")
]
