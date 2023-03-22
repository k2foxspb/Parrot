from django.urls import path, include

from parrotApp import views

urlpatterns = [
    path('', views.GeneralView.as_view())]