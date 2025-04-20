from django.urls import path
from .views import employee_create
urlpatterns=[
    path('employee/create/',employee_create,name='employee-name')
]