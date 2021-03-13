from django.shortcuts import render
# from rest_framework.permissions import AllowAny
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import action
from rest_framework import generics,status
from datetime import datetime as dt
from .models import EventInfo
from .serializers import EventInfoSerializers

# Create your views here.

class EventViewSet(generics.GenericAPIView):
    queryset = EventInfo.objects.all()
    serializer_class = EventInfoSerializers
    # permission_classes = (AllowAny, )
    # @action(methods=['POST'], detail=False)
    def post(self, request):
        if request.method == 'POST':
            title = request.data['title']
            description = request.data['description']
            event_pic = request.data['event_pic']
            seat_limit = request.data['seat_limit']
            created = request.data.get('created', dt.now())
            ends_on = request.data['ends_on']
            begins_on = request.data['begins_on']
            deadline = request.data['deadline']
            registered_num = 0
            # user_id = request.data['user_id']
            try:
                event = EventInfo(title=title, registered_num=registered_num, description=description, event_pic=event_pic, seat_limit=seat_limit, created=created, begins_on=begins_on, ends_on=ends_on, deadline=deadline)
        #return HttpResponse("Create Event")
                event.save()
                serial = EventInfoSerializers(event)
                return JsonResponse({'event':serial.data}, status = status.HTTP_201_CREATED)
            except Exception:
                raise ValueError("Invalid request")
        