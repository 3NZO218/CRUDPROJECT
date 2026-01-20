from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/', include('accounts.urls')),  # Your custom signup/login/etc.
    path('auth/', include('django.contrib.auth.urls')),  # Django built-in auth
]


