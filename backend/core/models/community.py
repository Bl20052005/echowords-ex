from django.db import models

class UserModel(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, blank=False, max_length=64)
    pw = models.CharField(unique=True, blank=False, max_length=256)

class LearnProgModel(models.Model):
    pid = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    
class ReaderModel(models.Model):
    pass