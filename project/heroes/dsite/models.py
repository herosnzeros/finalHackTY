from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    name = models.CharField(max_length=30)
    creator = models.ForeignKey(User, related_name="created")
    guest = models.ForeignKey(User)

