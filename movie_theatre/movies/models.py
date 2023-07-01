from django.db import models
# Create your models here.
class Movie(models.Model):
    movieTitle = models.CharField(max_length=512,blank=True)
    movieAdvisory = models.CharField(max_length=512,blank=True)
    movieImgUrl = models.CharField(max_length=512,blank=True)
    movieDuration = models.IntegerField(blank=True)
    buyTicketUrl = models.CharField(max_length=512,blank=True)

    def __str__(self):
        return self.movietitle