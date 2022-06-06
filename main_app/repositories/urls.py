from django.urls import path
from main_app.repositories import views

urlpatterns = [
    path('', views.repository_list, name="repository_list"),
    path('<int:pk>/', views.repository_detail, name="repository_detail"),
]