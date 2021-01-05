from django.db import models

# Create your models here.

class SubwayUsage(models.Model):
    Date = models.CharField(max_length=10)
    SubLine = models.CharField(max_length=15)
    SubStation = models.CharField(max_length=50)
    pass_on_board = models.IntegerField
    dise_pass = models.IntegerField

    def __str__(self):
        return self.SubStation