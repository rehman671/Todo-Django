from django.urls import path , include
from rest_framework import routers
from api.views import UserViewSet , TaskViewSet  , LogoutView 
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = routers.DefaultRouter()

router.register(r'user',UserViewSet)
router.register(r'task',TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('logout/' , LogoutView.as_view() , name ='logout'),
    path('refresh/' , TokenRefreshView.as_view() , name ='refresh'),
    
]


