

from django.db import models
class Jobs(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    vacancy=models.IntegerField()
    def __str__(self):
        return self.title
  

# Create your models here.
