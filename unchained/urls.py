from django.urls import path, include
from rest_framework import routers
from Business import views

router = routers.DefaultRouter()
router.register(r'businesses', views.BusinessViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'business-employees', views.BusinessEmployeeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]