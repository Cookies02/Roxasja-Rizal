from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('activity-1/', views.activity_1, name='activity_1'),
]