from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.index, name='index'),
    path('slave/', views.index, name='slave'),
    path('slave_view/', views.slave_view.as_view(), name='slave_view'),
    path('slave_check/', views.get_slave_check, name='slave_check'),
]
