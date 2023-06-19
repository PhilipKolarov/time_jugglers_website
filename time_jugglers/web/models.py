from django.db import models


class Profile(models.Model):
    username = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
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


class Order(models.Model):
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"

    QTY_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    SIZE_CHOICES = (
        (S, S),
        (M, M),
        (L, L),
        (XL, XL),
    )

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    address = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    city = models.CharField(
        max_length=40,
        null=False,
        blank=False,
    )

    country = models.CharField(
        max_length=40,
        null=False,
        blank=False,
    )

    postcode = models.CharField(
        max_length=10,
        null=False,
        blank=False,
    )

    quantity = models.IntegerField(
        choices=QTY_CHOICES,
        null=False,
        blank=False,
    )

    size = models.CharField(
        choices=SIZE_CHOICES,
        null=True,
        blank=True,
    )


class Contact(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    subject = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )

    text = models.TextField(
        null=False,
        blank=False,
    )


class Event(models.Model):
    JAN = "JAN"
    FEB = "FEB"
    MAR = "MAR"
    APR = "APR"
    MAY = "MAY"
    JUN = "JUN"
    JUL = "JUL"
    AUG = "AUG"
    SEP = "SEP"
    OCT = "OCT"
    NOV = "NOV"
    DEC = "DEC"

    DAY_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17),
        (18, 18),
        (19, 19),
        (20, 20),
        (21, 21),
        (22, 22),
        (23, 23),
        (24, 24),
        (25, 25),
        (26, 26),
        (27, 27),
        (28, 28),
        (29, 29),
        (30, 30),
        (31, 31),
    )

    MONTH_CHOICES = (
        (JAN, JAN),
        (FEB, FEB),
        (MAR, MAR),
        (APR, APR),
        (MAY, MAY),
        (JUN, JUN),
        (JUL, JUL),
        (AUG, AUG),
        (SEP, SEP),
        (OCT, OCT),
        (NOV, NOV),
        (DEC, DEC),
    )

    day = models.IntegerField(
        choices=DAY_CHOICES,
        null=False,
        blank=False,
    )

    month = models.CharField(
        choices=MONTH_CHOICES,
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )
