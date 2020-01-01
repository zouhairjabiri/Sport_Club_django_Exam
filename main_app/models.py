from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENRE_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class Adherent(User):
    Email = models.CharField(max_length=20,primary_key=True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=200)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    tel = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Sport(models.Model):
    designation = models.CharField(max_length=100, primary_key=True)
    tarif = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.designation


class Inscription(models.Model):
    Email = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    designation = models.ForeignKey(Sport, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('Email', 'designation'),)

    def __str__(self):
        return str(self.Email) + ', ' + str(self.designation)
