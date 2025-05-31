from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):

    class Genre(models.TextChoices):
        ROCK = 'ROCK', 'Rock'
        POP = 'POP', 'Pop'
        JAZZ = 'JAZZ', 'Jazz'
        CLASSICAL = 'CLASSICAL', 'Classical'
        HIP_HOP = 'HIP_HOP', 'Hip Hop'
        ELECTRONIC = 'ELECTRONIC', 'Electronic'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=20, default=Genre.ROCK)
    biography = models.fields.CharField(max_length=1000, default='No biography provided')
    year_formed = models.fields.IntegerField(
        default=2021,
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Listing(models.Model):
    title = models.fields.CharField(max_length=100)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
  