from django.shortcuts import render
# from rest_framework.permissions import AllowAny
from django.http import HttpResponse,JsonResponse
# from rest_framework.decorators import action
from rest_framework import generics,status, permissions
from datetime import datetime as dt
from rest_framework.response import Response
from .models import EventInfo
from .serializers import EventInfoSerializers

# Create your views here.

class EventWritePermission(permissions.BasePermission):
    message = "Editing is only restricted to the Author"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_id == request.user
    

class EventViewSet(generics.GenericAPIView):
    queryset = EventInfo.objects.all()
    serializer_class = EventInfoSerializers
    permission_classes = (permissions.IsAuthenticated, )
    # @action(methods=['POST'], detail=False)
    def post(self, request):
        if request.method == 'POST':
            title = request.data['title']
            description = request.data['description']
            event_pic = request.FILES.get('event_pic', "")
            seat_limit = request.data.get('seat_limit', 0)
            # created = request.data.get('created', dt.now())
            ends_on = request.data.get('ends_on', "2018-03-29T13:34:00.000")
            begins_on = request.data.get('begins_on', "2018-03-29T13:30:00.000")
            deadline = request.data.get('deadline', "2018-03-29T13:34:00.000")
            registered_num = 0
            # user_id = request.data['user_id']
            try:
                event = EventInfo(title=title, registered_num=registered_num, user=request.user, description=description, event_pic=event_pic, seat_limit=seat_limit, begins_on=begins_on, ends_on=ends_on, deadline=deadline)
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
            return JsonResponse(ser.data, safe=False)
        else:
            return JsonResponse({"message":"No Event Currently"})

class EventByUserView(generics.GenericAPIView):
    queryset = EventInfo.objects.all()
    serializer_class = EventInfoSerializers
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        try:
            events = EventInfo.objects.filter(user_id=request.user.id)
            if events:
                ser = EventInfoSerializers(events, many=True)
                return JsonResponse(ser.data, safe=False)
            else:
                return JsonResponse({"message":"No Event Currently"})
        except Exception:
            return JsonResponse({"error":"Something went wrong"})   
class EventViewByID(generics.GenericAPIView, EventWritePermission):
    queryset = EventInfo.objects.all()
    serializer_class = EventInfoSerializers
    permission_classes = [permissions.IsAuthenticated]
    
    # def get_queryset(self):
    #     return super(EventViewByID, self).filter(user=self.request.user)
    def get(self, request, pk):
        
        try:
            event = EventInfo.objects.get(id=pk)
            if event:
                ser = EventInfoSerializers(event)
                return JsonResponse({"user":ser.data, "user_logged":request.user.id})
            else:
                return JsonResponse({"error":"Event Doesnot Exist"})
        except Exception:
            return JsonResponse({"error":"invalid Request"})
    def put(self, request, pk):
    
        try:
            event = EventInfo.objects.get(id=pk)
            if event.user_id == request.user.id:
                title = request.data.get('title', event.title)
                desc = request.data.get('description', event.description)
                seat = request.data.get('seat_limit', event.seat_limit)
                event.title = title
                event.description = desc
                event.seat_limit = seat
                event.save()

                ser = EventInfoSerializers(event)
                return JsonResponse({"event":ser.data}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({"error":"User isnot able to edit the event"})
        except Exception:
            return JsonResponse({"error":"Event Doesnot exist"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, pk):
        try:
            event = EventInfo.objects.get(id=pk)
            if request.user.id == event.user_id:
                event.delete()
                return JsonResponse({"message":"Event Deleted Sucesfully"}, status=status.HTTP_204_NO_CONTENT)
            else:
                return JsonResponse({"error":"You cant delete this event"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({"error":"Event Doesnot Exist"}, status=status.HTTP_404_NOT_FOUND)