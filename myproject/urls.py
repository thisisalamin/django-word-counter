
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('wordcount.urls')),
    path('admin/', admin.site.urls),
]
