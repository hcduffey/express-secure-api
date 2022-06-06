from django.urls import path
from main_app.vulnerabilities import views

urlpatterns = [
    path('', views.vulnerability_list, name="vulnerability_list"),
    path('<int:pk>/', views.vulnerability_detail, name="vulnerability_detail"),
]