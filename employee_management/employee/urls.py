'''employee urls code is'''
from django.urls import path
from employee import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('employee/', views.EmployeeViewSet.as_view(), name="employee_create"),
    path(r'employee-detail/<int:pk>/',
         views.EmployeeDetail.as_view(), name="employee_list"),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path(r'api/users', views.UserCreate.as_view(), name='account-create'),
    path(r'api/employee-detail-pagination', views.EmployeeDetailPaginationView.as_view(), name='account-create'),
]
