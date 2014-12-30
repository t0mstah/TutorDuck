from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)
    salt = models.CharField(max_length=100)


class TutorCard(models.Model):
    tutor = models.ForeignKey(User)
    first_name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    tagLine = models.CharField(max_length=200)
    description = models.CharField(max_length=200)