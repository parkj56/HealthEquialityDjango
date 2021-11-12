from django.urls import path
from . import views

urlpatterns = [
    path('health_equality/', views.AllData.as_view()),
    path('health_equality/<int:pk>/', views.BodyDetail.as_view())]