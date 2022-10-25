from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'myJXN'
urlpatterns = [
    path('', views.myview, name='myview'),
    path('report/', views.report, name = 'report'),
    path('register/',views.register,name= 'register'),
]