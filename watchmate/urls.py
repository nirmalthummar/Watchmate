from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('watchlist_app.api.urls')),
    path('watch/', include('movieapp.api.urls')),
    path('account/', include('user_app.api.urls')),
    # path('api-auth/', include('rest_framework.urls')),
]
