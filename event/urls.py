from django.urls import path
# from django.conf.urls import include
# from rest_framework import routers
#  from .views import EventViewSet
from . import views

#from .serializers import EventInfoSerializers

# router = routers.DefaultRouter()
# router.register("create", views.EventViewSet, basename="create")

urlpatterns = [
    path('createEvent', views.EventViewSet.as_view())
    # path('deleteEvent/:id', views.delete_event, name='delete Event'),
    # path('updateEvent/:id', views.update_event, name='update Event'),
    # path("getEvents", views.get_events, name='get Events')
    # path("", include(router.urls))
]
