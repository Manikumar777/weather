from django.db import models
from rest_framework.authtoken.admin import User


# Create your models here.
class City(models.Model):

    name = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
        class Meta:
            verbose_name_plural = 'cities'
class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.IntegerField()

    def __str__(self):
        return self.city

# class SearchHistory(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     query = models.CharField(max_length=100)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.query


