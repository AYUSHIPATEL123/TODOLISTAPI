from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import TaskViewSet,RegisterView,LoginView
from rest_framework_simplejwt.views import TokenRefreshView ,TokenObtainPairView
router = routers.DefaultRouter()
router.register(r'tasks',TaskViewSet,basename='task')
router.register(r'register',RegisterView,basename='register')

urlpatterns = [
   path('',include(router.urls)),
   path('login/',LoginView.as_view(),name='login'),
   path('token/',TokenObtainPairView.as_view(),name='token'), 
   path('token/refresh/',TokenRefreshView.as_view(),name='refresh_token'), 
]
