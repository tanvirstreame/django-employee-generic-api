'''employee urls code is'''
from django.urls import path
from employee import views

urlpatterns = [
    path('user/', views.UserViewSet.as_view(), name="user-create"),
    path(r'user-detail/<int:pk>/', views.UserDetail.as_view(), name="user-list"),
]
