from django.urls import path

from travelapp import views

urlpatterns = [

    path('',views.static,name='static'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

]