from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('assignment/<int:pk>',views.AssignmentApiView.as_view())
]