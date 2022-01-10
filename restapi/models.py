from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save
)


class Banks(models.Model):
    n_of_or = models.CharField(max_length=100)
    op_dt = models.DateField()
    capital = models.CharField(max_length=100)
    ceo_of_cmp = models.CharField(max_length=100)
    ser_es = models.CharField(max_length=500)
    cards = models.CharField(max_length=300)
    n_of_br = models.IntegerField()
    n_of_emp = models.IntegerField()
    aff_com = models.CharField(null=True, blank=True, max_length=500)


@receiver(post_save, sender=User)
def ser_password(sender, instance, *args, **kwargs):
    password = make_password(instance.password)
    User.objects.filter(pk=instance.id).update(password=password)


#  08/01/2022  #


class Student(models.Model):
    gender_list = (
        ('male', 'male'),
        ('female', 'female')
    )
    lang_list = (
        ('ru', 'ru'),
        ('uz', 'uz'),
        ('en', 'en')
    )
    course_list = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    )

    firstname = models.CharField(max_length=50)
    secondname = models.CharField(max_length=60)
    language = models.CharField(choices=lang_list, max_length=10)
    cource = models.IntegerField(choices=course_list)
    gpa = models.FloatField()
    gender = models.CharField(choices=gender_list, max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.firstname} - {self.secondname} - {self.cource}'

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

