from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.user_login,name="login"),
    path('register/', views.user_login,name="register"),
    path('dashboard/', views.user_dashboard,name="dashboard"),
    path('logout/', views.user_logout,name="logout"),
   
   
]