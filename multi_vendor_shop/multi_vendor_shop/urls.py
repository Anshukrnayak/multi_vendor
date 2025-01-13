
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path




urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('account/',include('account.urls'))
]

# urls.py

# This will serve media files in development mode (not for production)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
