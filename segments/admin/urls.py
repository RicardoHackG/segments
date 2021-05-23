"""
Segments admin URL Configuration
"""
from django.contrib import admin
from django.urls import path

admin.site.site_header = "Segments Administration"
admin.site.site_title = "Admin"
admin.site.index_title = "Segments"

urlpatterns = [
    path('admin/', admin.site.urls),
]