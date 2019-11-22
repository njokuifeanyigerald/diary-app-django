from django.contrib import admin
from django.urls import path
from project.views import home,add
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('add/', add, name="add"),
]
