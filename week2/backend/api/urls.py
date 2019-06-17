from django.urls import path
from api import views

urlpatterns = [
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('', views.home),
    path('users/', views.UserList.as_view(), name='users'),
    path('login/', views.login),
    path('logout/', views.logout),

]
