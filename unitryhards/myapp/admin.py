from django.contrib import admin
from .models import University, Department, Course, Paper

admin.site.register(University)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Paper)