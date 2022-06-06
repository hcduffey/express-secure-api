from django.urls import path
from main_app.languages import views

urlpatterns = [
    path('', views.language_list, name="language_list"),
    path('<int:pk>/', views.language_detail, name="language_detail"),
]