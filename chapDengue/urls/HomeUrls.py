from django.urls import path
from chapDengue.views.HomeView import home_view

urlpatterns = [
    path("", home_view),
]
