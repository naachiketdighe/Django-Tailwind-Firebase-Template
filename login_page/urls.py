from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Add this line
    path('home/', views.home, name='home'),
    path('find_bar/', views.find_bar, name='find_bar'),
    path('host_bar/', views.host_bar, name='host_bar'),
    path('friends/', views.friends, name='friends'),

]
