from django.db import models

# Create your models here.
class Setup(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    minimumPlayers = models.IntegerField(default = 8)
    maximumPlayers = models.IntegerField(default = 12)
    featuredSetup = models.BooleanField(default = False)
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255) 
    alignment = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    action = models.CharField(max_length=1024, null=True, default=None)
    setup = models.ManyToManyField(Setup, through='SetupRole', related_name="roles")
    def __str__(self):
        return self.name

class SetupRole(models.Model):
    setup = models.ForeignKey(Setup)
    role = models.ForeignKey(Role)

