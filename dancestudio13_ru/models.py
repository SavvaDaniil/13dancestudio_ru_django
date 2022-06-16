#from msilib.schema import Class
from tabnanny import verbose
from typing import Iterable, Optional
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.contrib import admin
import os
import datetime
from django.utils import timezone
from numpy import delete

# Create your models here.


class VideoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "active")

class Video(models.Model):

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
    
    def getPosterPath(instance, filename) -> str:
        name_of_file = instance.id
        if name_of_file is None:
            name_of_file = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        return ...

    def getVideoPath(instance, filename) -> str:
        #instance.name = filename
        name_of_file = instance.id
        instance.filename_basic = filename
        if name_of_file is None:
            name_of_file = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        return ...

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=516, blank=True, null=True)
    filename_basic = models.CharField(max_length=516, blank=True, null=True, editable=False)
    active = models.BooleanField(default=False)
    posterSrc = models.ImageField(upload_to = getPosterPath, null=True, blank=True)
    videoSrc = models.FileField(upload_to = getVideoPath, null=True, blank=True)
    
    def getPosterSrc(self) -> str:
        if not self.posterSrc:
            return None
        return self.posterSrc.url

    def __str__(self) -> str:
        return "{0}. {1}".format(self.id, self.name)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "active", "order_number")

class Teacher(models.Model):

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def getPosterPath(instance, filename) -> str:
        return ...

    readonly_fields = ["date_of_add", "date_of_update"]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    order_number = models.IntegerField(default=1, blank=True, null=True)
    link_short = models.CharField(max_length=516, null=True, blank=True)
    active = models.BooleanField(default=0)
    schedule_as_str = models.CharField(max_length=256, null=True, blank=True)
    date_of_add = models.DateTimeField(null=True, blank=True, editable=False)
    date_of_update = models.DateTimeField(null=True, blank=True, editable=False)
    posterSrc = models.ImageField(upload_to = getPosterPath, null=True, blank=True)
    videos = models.ManyToManyField(Video, blank=True)

    def __str__(self) -> str:
        return "{0}. {1}".format(self.id, self.name)

    def save(self, *args, **kwargs):

        if self.date_of_add is None:
            self.date_of_add = datetime.datetime.now(tz=timezone.utc)
        self.date_of_update = datetime.datetime.now(tz=timezone.utc)

        #if self.posterSrc is not None:
            #print("posterSrc.path:", self.posterSrc.path)
            #storage, path = self.posterSrc.storage, self.posterSrc.path
            #storage.delete(path)

        super(Teacher, self).save(*args, **kwargs)

    def getPosterSrc(self) -> str:
        if not self.posterSrc:
            return None
        return self.posterSrc.url





class StyleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "order_number")


class Style(models.Model):

    class Meta:
        verbose_name = "Стиль"
        verbose_name_plural = "Стили"
    
    def getPosterPath(instance, filename) -> str:
        return ...

    def getVideoPath(instance, filename) -> str:
        #instance.name = filename
        name_of_file = instance.id
        instance.filename_basic = filename
        if name_of_file is None:
            name_of_file = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        return ...

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=516, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link_short = models.CharField(max_length=516, null=True, blank=True)
    active = models.BooleanField(default=False)
    posterSrc = models.ImageField(upload_to = getPosterPath, null=True, blank=True)
    video = models.ForeignKey(Video, on_delete = models.CASCADE, blank=True, null=True)
    order_number = models.IntegerField(default=1, blank=True, null=True)
    teachers = models.ManyToManyField(Teacher, blank=True)
    
    is_bigger = models.BooleanField(default=False)
    is_lower = models.BooleanField(default=False)


    def getPosterSrc(self) -> str:
        if not self.posterSrc:
            return None
        return self.posterSrc.url

    def __str__(self) -> str:
        return "{0}. {1}".format(self.id, self.name)



class AbonementAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "order_number")

class Abonement(models.Model):
    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512, null=True, blank=True)
    active = models.BooleanField(default=False)
    price = models.IntegerField(blank=True, default=0)
    order_number = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self) -> str:
        return "{0}. {1}".format(self.id, self.name)


class RentHallAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "order_number")

class RentHall(models.Model):
    class Meta:
        verbose_name = "Зал в аренду"
        verbose_name_plural = "Залы в аренду"
    
    def getPoster0Path(instance, filename) -> str:
        return 'image/rent_hall/0/{0}.jpg'.format(instance.id)
    def getPoster1Path(instance, filename) -> str:
        return 'image/rent_hall/1/{0}.jpg'.format(instance.id)
    def getPoster2Path(instance, filename) -> str:
        return 'image/rent_hall/2/{0}.jpg'.format(instance.id)

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=516, null=True, blank=True)
    active = models.BooleanField(default=False)
    posterSrc0 = models.ImageField(upload_to = getPoster0Path, null=True, blank=True)
    posterSrc1 = models.ImageField(upload_to = getPoster1Path, null=True, blank=True)
    posterSrc2 = models.ImageField(upload_to = getPoster2Path, null=True, blank=True)
    order_number = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self) -> str:
        return "{0}. {1}".format(self.id, self.name)

    def getPosterSrc0(self) -> str:
        if not self.posterSrc0:
            return None
        return self.posterSrc0.url

    def getPosterSrc1(self) -> str:
        if not self.posterSrc1:
            return None
        return self.posterSrc1.url

    def getPosterSrc2(self) -> str:
        if not self.posterSrc2:
            return None
        return self.posterSrc2.url


class DanceGroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "active", "isMonday", "isTuesday", "isWednesday", "isThursday", "isFriday", "isSaturday", "isSunday")

class DanceGroup(models.Model):

    class Meta:
        verbose_name = "Группа в расписании"
        verbose_name_plural = "Расписание"


    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=516, null=True, blank=True)
    level = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(3),
            MinValueValidator(1)
        ]
    )
    isSpecialCourse = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    
    ...

    style = models.ForeignKey(Style, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)




class UserZayavkaAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "date_of_add")


class UserZayavka(models.Model):
    
    class Meta:
        verbose_name = 'Заявка с сайта'
        verbose_name_plural = 'Заявки с сайта'

    readonly_fields = ["date_of_add", "date_of_update"]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=256, null=True, blank=True)
    ip_address = models.CharField(max_length=64, null=True, blank=True)
    date_of_add = models.DateTimeField(null=True, blank=True, editable=False)



