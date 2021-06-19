from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('domain/', include('Domain.urls')),
    path('acount/', include('User.urls')),
]
