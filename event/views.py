from django.shortcuts import render
from rest_framework.permissions import AllowAny
from django.http import HttpResponse,JsonResponse
# from rest_framework.decorators import action
from rest_framework import generics,status
from datetime import datetime as dt
from .models import EventInfo
from .serializers import EventInfoSerializers

# Create your views here.

class EventViewSet(generics.GenericAPIView):
    queryset = EventInfo.objects.all()
    serializer_class = EventInfoSerializers
    permission_classes = (AllowAny, )
    # @action(methods=['POST'], detail=False)
    def post(self, request):
        if request.method == 'POST':
            title = request.data['title']
            description = request.data['description']
            event_pic = request.data['event_pic']
            seat_limit = request.data['seat_limit']
            # created = request.data.get('created', dt.now())
            ends_on = request.data['ends_on']
            begins_on = request.data['begins_on']
            deadline = request.data['deadline']
            registered_num = 0
            # user_id = request.data['user_id']
            try:
                event = EventInfo(title=title, registered_num=registered_num, description=description, event_pic=event_pic, seat_limit=seat_limit, begins_on=begins_on, ends_on=ends_on, deadline=deadline)
        #return HttpResponse("Create Event")
                event.save()
                serial = EventInfoSerializers(event)
                return JsonResponse({'event':serial.data}, status = status.HTTP_201_CREATED)
            except Exception:
                raise ValueError("Invalid request")
    def get(self, request):
        event = EventInfo.objects.all()

        if event:
            ser = EventInfoSerializers(event, many=True)
            return JsonResponse({"events":ser.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"message":"No Event Currently"})

class EventViewByID(generics.GenericAPIView):
    queryset = EventInfo.objects.all()
    serializer_class = EventInfoSerializers
    permission_classes = (AllowAny, )
    def get(self, request, pk):
        try:
            event = EventInfo.objects.get(id=pk)
            if event:
                ser = EventInfoSerializers(event)
                return JsonResponse({"event":ser.data}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"error":"Event Doesnot Exist"})
        except Exception:
            return JsonResponse({"error":"Event Doesnot Exist"})
    def put(self, request, pk):
        try:
            event = EventInfo.objects.get(id=pk)
            if event:
                title = request.data.get('title', event.title)
                desc = request.data.get('description', event.description)
                seat = request.data.get('seat_limit', event.seat_limit)
                event.title = title
                event.description = desc
                event.seat_limit = seat
                event.save()

                ser = EventInfoSerializers(event)
                return JsonResponse({"event":ser.data}, status=status.HTTP_201_CREATED)
        except Exception:
            return JsonResponse({"error":"Event Doesnot exist"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, pk):
        try:
            event = EventInfo.objects.get(id=pk)
            if event:
                event.delete()
                return JsonResponse({"message":"Event Deleted Sucesfully"}, status=status.HTTP_204_NO_CONTENT)
            else:
                return JsonResponse({"error":"Event Doesnot Doesnot exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({"error":"Event Doesnot Exist"}, status=status.HTTP_404_NOT_FOUND)