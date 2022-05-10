from django.urls import include, path, re_path
#from DjangoAPI.DjangoAPI.settings import MEDIA_ROOT, MEDIA_URL
from EmployeeApp import views
from django_urls import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    re_path(r'^department$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),
    re_path(r'^employee$',views.employeeApi),
    re_path(r'^employee/([0-9]+)$',views.employeeApi),
    re_path(r'^employee/savefile',views.SaveFile)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)