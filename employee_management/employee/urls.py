'''employee urls code is'''
from django.urls import path
from employee import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('user/', views.UserViewSet.as_view(), name="user_create"),
    path(r'user-detail/<int:pk>/', views.UserDetail.as_view(), name="user_list"),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
