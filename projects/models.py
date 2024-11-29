from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 200)
    rut = models.CharField(max_length = 200)
    members = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)

