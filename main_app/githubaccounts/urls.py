from django.urls import path, include
from main_app.githubaccounts import views

urlpatterns = [
    path('', views.github_account_list, name="githubaccount_list"),
    path('<int:pk>/', views.githubaccount_detail, name="githubaccount_detail"),
]