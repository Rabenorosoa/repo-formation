from django.contrib import admin
from django.urls import path
from myApp import views

app_name = 'myApp'

urlpatterns = [
    path('', views.indexView , name='home'),
    path('details/<int:id>/', views.detailsView , name='details'),
    path('newPost/', views.newPostView , name='newPost'),
    path('updatePost/<int:id>/', views.updateView , name='updatePost'),
    path('deletePost/<int:id>/', views.deleteView , name='deletePost'),
    path('search/', views.searchview , name='search'),
]