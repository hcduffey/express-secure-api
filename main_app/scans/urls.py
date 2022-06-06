from django.urls import path
from main_app.scans import views

urlpatterns = [
    path('', views.scan_list, name="scan_list"),
    path('<int:pk>/', views.scan_detail, name="scan_detail"),
]