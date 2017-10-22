from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.


def pp_upload_path(instance,filename):
    return '/'.join(['Alumni_profile_pictures', str(instance.id), filename])


class University(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return "%s" % self.name


class Alumni(AbstractUser):
    summary = models.TextField(max_length=800)
    profile_picture = models.ImageField(upload_to=pp_upload_path,default='no-icon.png')
    university = models.ForeignKey(University,default=1)
    department = models.CharField(max_length=300,default="Bilgisayar Bilişimi")

    YEAR_CHOICES = [(r, r) for r in range(1950, timezone.datetime.today().year)]

    year_graduated = models.IntegerField(choices=YEAR_CHOICES, default=timezone.now().year)

    def __str__(self):
        return "%s %s" % (self.first_name,self.last_name)


class Club(models.Model):
    name = models.CharField(max_length=300)
    members = models.ManyToManyField(Alumni)

    def __str__(self):
        return "%s" % self.name


class Message(models.Model):
    yazan = models.CharField(max_length=200)
    to = models.ForeignKey(Alumni)
    mesaj = models.TextField(max_length=440)