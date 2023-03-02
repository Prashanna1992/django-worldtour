from django.db import models

# Create your models here.
class Trip(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    nights = models.IntegerField()
    price = models.FloatField()
    
    def __str__(self):
        return f"{self.id} : {self.origin} To {self.destination}, For {self.nights} Nights. Cost : {self.price} EUR"
