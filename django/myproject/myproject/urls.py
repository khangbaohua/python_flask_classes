from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path("lalala/",views.lalala),
    path("banana/",include("student.urls"))
]

