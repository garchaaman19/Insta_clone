from django.urls import path
from .views import CreateUserAPI


urlpatterns=[path('createuser',CreateUserAPI.as_view())]