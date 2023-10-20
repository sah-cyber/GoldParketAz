
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . settings import DEBUG
from homeparket.views import ErorView
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homeparket.urls')),
]

handler404 = ErorView.as_view()


if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

