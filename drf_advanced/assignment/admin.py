from django.contrib import admin

from .models import Category, Assignment, Submission

# Register your models here.
admin.site.register(Category)
admin.site.register(Assignment)
admin.site.register(Submission)