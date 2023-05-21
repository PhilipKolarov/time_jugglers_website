from django.core import validators
from django.db import models


class Album (models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        null=False,
        blank=False,
    )

    tracks_count = models.IntegerField(
        null=False,
        blank=False,
    )

    length = models.TimeField(
        null=False,
        blank=False,
    )

    recorded = models.CharField(
        null=False,
        blank=False,
    )

    mixed = models.CharField(
        null=True,
        blank=True,
    )

    mastered = models.CharField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    price = models.IntegerField(
        null=False,
        blank=False,
    )

    image = models.ImageField(
        upload_to='/time_jugglers/staticfiles/images/merch-items',
        null=False,
        blank=False,
    )

