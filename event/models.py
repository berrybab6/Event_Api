from django.db import models
# from users.models import UserInfo

# Create your models here.
class EventInfo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    event_pic = models.URLField()
    seat_limit = models.PositiveIntegerField()
    registered_num = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now=True)
    begins_on = models.DateTimeField()
    ends_on = models.DateTimeField()
    deadline = models.DateTimeField()
    # user = models.ForeignKey(UserInfo, on_delete=models.CASCADE,null=False)
    class Meta:
        ordering=['created']