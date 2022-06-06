from django.urls import path
from main_app.branches import views

urlpatterns = [
    path('', views.branch_list, name="branch_list"),
    path('<int:pk>/', views.branch_detail, name="branch_detail"),
]