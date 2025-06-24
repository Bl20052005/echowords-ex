from django.db import models

class LangEnum(models.TextChoices):
    SPANISH = ("SP", "Spanish")

class UserModel(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, blank=False, max_length=64)
    pw = models.CharField(unique=True, blank=False, max_length=256)
    
    t_create = models.DateTimeField(auto_now_add=True)
    t_access = models.DateTimeField(auto_now_add=True)

class LearnProgModel(models.Model):
    pid = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    lang = models.CharField(max_length=2, blank=False, choices=LangEnum)

    st_wc = models.IntegerField(blank=False, default=0)

    t_create = models.DateTimeField(auto_now_add=True)
    t_access = models.DateTimeField(auto_now_add=True)
    
class ReaderModel(models.Model):
    rid = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    prog = models.ForeignKey(LearnProgModel, null=True, on_delete=models.DO_NOTHING)

class WordRecordModel(models.Model):
    pass