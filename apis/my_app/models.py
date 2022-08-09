from django.db import models

# Create your models here.
class RotaryclubVolunteerList(models.Model):
    volunteer_name = models.CharField(max_length=50)
    past_socialwork = models.CharField(max_length=100)
    age = models.IntegerField()
