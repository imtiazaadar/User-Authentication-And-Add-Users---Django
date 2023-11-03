from django.contrib import admin
from django.urls import path, include
from userauthenapp import views
# Name : Imtiaz Adar
# Project : User Authentication And Adding Users
# Language : Python
# Framework : Django
# Phone : 01778767775, 01979777379
# Email : imtiazadarofficial@gmail.com
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage, name='index'),
    path('index/', views.HomePage, name='index'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('logout/', views.Logout, name='logout'),
    path('showinfo/', views.ShowInformation, name='showinfo'),
    path('addinformation/', views.AddInformation, name='addinformation'),
]
