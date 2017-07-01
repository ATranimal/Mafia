from django.db import models

# Create your models here.
class Setup(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    playerNumber = models.IntegerField(default = 0)
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255) 
    allignment = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    setup = models.ManyToManyField(Setup, through='SetupRole', related_name="roles")
    def __str__(self):
        return self.name

class SetupRole(models.Model):
    setup = models.ForeignKey(Setup)
    role = models.ForeignKey(Role)

