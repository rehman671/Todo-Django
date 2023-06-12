from django.urls import path , include
from rest_framework import routers
from api.views import UserViewSet , TaskViewSet ,LoginViewSet , logout_view

router = routers.DefaultRouter()

router.register(r'user',UserViewSet)
router.register(r'task',TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/' , LoginViewSet.as_view() , name='login'),
    path('logout/' , logout_view , name='logout')
    
]


