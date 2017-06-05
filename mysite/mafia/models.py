from django.db import models

# Create your models here.
class Setup(models.Model):
    name = models.CharField(max_length=255)
    playerNumber = models.IntegerField(default = 0)
    def __str__(self):
        return self.name



class Role(models.Model):
    name = models.CharField(max_length=255)
    allignment = models.CharField(max_length=255)
    setup = models.ManyToManyField(Setup)
    def __str__(self):
        return self.name

