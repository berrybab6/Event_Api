from django.shortcuts import render
from rest_framework.permissions import AllowAny
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import action
from rest_framework import viewsets,status
from datetime import datetime as dt
from .models import EventInfo
from .serializers import EventInfoSerializers

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = EventInfo.objects.all()
    serializer_class = EventInfoSerializers
    permission_classes = (AllowAny, )
    @action(methods=['POST'], detail=False)
    def create_event(self, request, pk=None):
        if request.method == 'POST':
            title = request.data['title']
            description = request.data['description']
            event_pic = request.data['event_pic']
            seat_limit = request.data['seat_limit']
            created = request.data['created']
            ends_on = request.data['ends_on']
            begins_on = request.data['begins_on']
            deadline = request.data['deadline']
            registered_num = 0
            user_id = request.data['user_id']

            event = EventInfo(title=title, registered_num=registered_num, description=description, event_pic=event_pic, seat_limit=seat_limit, created=created, begins_on=begins_on, ends_on=ends_on, deadline=deadline, user_id=user_id)
        #return HttpResponse("Create Event")
            event.save()
            return JsonResponse({'event':event})
