# jobsearch/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("main_page/<int:page>/", views.main_page, name="main_page"),
]
