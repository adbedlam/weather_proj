from django.db import models

# Create your models here.
class CitySearch(models.Model):
    city = models.CharField(max_length=100)
    searched_at = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city} @ {self.searched_at}"