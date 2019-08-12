from django.urls import path, include
from rest_framework import routers
from Business import views
from Business.views import CustomAuthToken
from django.conf.urls import url
#from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'businesses', views.BusinessViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'business-employees', views.BusinessEmployeeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    #url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-token-auth/', CustomAuthToken.as_view())
]