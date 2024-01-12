from django.urls import path
from . import views

app_name = 'baankapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('success_page/', views.success_page, name='success_page'),
    path('newpage/', views.newpage, name='newpage'),
    # path('showpage/', views.showpage, name='showpage'),

]
