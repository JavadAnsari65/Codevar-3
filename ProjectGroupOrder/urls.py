from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .view import *

urlpatterns = [
    path('', Home),
    path('Ws', WorkSamples),
    path('Gm', Members),
    path('M/',include('MemberGroup.urls',namespace='Member')),
    path('U/',include('User.urls',namespace='User')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
