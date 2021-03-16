from rest_framework import serializers
from .models import EventInfo

class  EventInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = EventInfo
        fields = ['id',
                  'title',
                  'description',
                  'event_pic',
                  'seat_limit',
                  'registered_num',
                  'created',
                  'begins_on',
                  'ends_on',
                  'deadline',
                  'user_id',
                  ]
