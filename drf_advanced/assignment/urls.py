from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create/',views.create_assignment),
    path('createsub/',views.create_submission),
    path('getassignment/',views.get_assignment),
    path('assignment/<int:pk>',views.AssignmentApiView.as_view()),
    path('assignment', views.AssignmentApiView.as_view()),
]