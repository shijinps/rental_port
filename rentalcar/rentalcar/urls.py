from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('adminapp.urls')),  # Fixed typo from 'adminapp.url' to 'adminapp.urls'
    path('accounts/', include('django.contrib.auth.urls')),
]

# Serve static files during development (e.g., CSS, JavaScript, images)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files during development (e.g., user-uploaded images)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
