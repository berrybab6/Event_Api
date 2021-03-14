from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
urlpatterns = [
    path('', views.index)
] 
urlpatterns += staticfiles_urlpatterns()
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
