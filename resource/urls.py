# Importing necessary modules & libraries
from django.urls import path
from resource import views


# Setting the app_name and url paths
app_name = "resource"
urlpatterns = [
    path('', views.index, name="index"),
]