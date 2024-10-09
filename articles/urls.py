from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'), 
    path('create/', views.create, name='create'), # C  
    path('<int:pk>/', views.read, name='read'), # R
    path('<int:pk>/update/', views.update, name='update'), # U
    path('<int:pk>/delete/', views.delete, name='delete'), # D 
]
