from django.db import models

class LangEnum(models.TextChoices):
    SPANISH = ("SP", "Spanish")

class UserModel(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, blank=False, max_length=64)
    pw = models.CharField(unique=True, blank=False, max_length=256)
    
    t_create = models.DateTimeField(auto_now_add=True)
    t_access = models.DateTimeField(auto_now_add=True)

class CompanionModel(models.Model):
    cid = models.AutoField(primary_key=True)
    u1 = models.ForeignKey(UserModel, related_name="u1", on_delete=models.DO_NOTHING)
    u2 = models.ForeignKey(UserModel, related_name="u2", on_delete=models.DO_NOTHING)

    t_create = models.DateTimeField(auto_now_add=True)

class LearnProgModel(models.Model):
    pid = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    lang = models.CharField(max_length=2, blank=False, choices=LangEnum)

    t_create = models.DateTimeField(auto_now_add=True)
    t_access = models.DateTimeField(auto_now_add=True)
    
class ReaderModel(models.Model):
    rid = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    prog = models.ForeignKey(LearnProgModel, null=True, on_delete=models.DO_NOTHING)

    t_create = models.DateTimeField(auto_now_add=True)
    t_access = models.DateTimeField(auto_now_add=True)

class ReaderChapterModel(models.Model):
    rcid = models.AutoField(primary_key=True)
    reader = models.ForeignKey(ReaderModel, on_delete=models.DO_NOTHING)

    t_create = models.DateTimeField(auto_now_add=True)
    t_access = models.DateTimeField(auto_now_add=True)

class VocabModel(models.Model):
    vid = models.AutoField(primary_key=True)
    lang = models.CharField(max_length=2, blank=False, choices=LangEnum)
    text = models.CharField(max_length=128, blank=False)

class VocabRecordModel(models.Model):
    vrid = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    prog = models.ForeignKey(LearnProgModel, on_delete=models.DO_NOTHING)
    of = models.ForeignKey(VocabModel, on_delete=models.DO_NOTHING)

    t_create = models.DateTimeField(auto_now_add=True)