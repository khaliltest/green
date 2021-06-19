from django.urls import path
from .views import OwnerRegister, AdvisorRegister, UserRegister
from rest_framework.authtoken.views import obtain_auth_token

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('oregister/', OwnerRegister, name='owner-register'),
    path('aregister/', AdvisorRegister, name='advisor-register'),
    path('uregister/', UserRegister, name='user-register'),
    path('login/', obtain_auth_token, name='login'),
    path('swagger/', schema_view),
]

