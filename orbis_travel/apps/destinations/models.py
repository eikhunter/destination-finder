from cms.apps.media.models import ImageRefField
from cms.apps.pages.models import ContentBase
from cms.models import PageBase
from django.db import models


class Destinations(ContentBase):

    urlconf = 'orbis_travel.apps.destinations.urls'

    def __str__(self):
        return self.page.title


class Destination(PageBase):

    page = models.ForeignKey(
        'destinations.Destinations',
    )

    image = ImageRefField(
        verbose_name='Image',
        blank=False,
        null=True,
    )

    weather = models.TextField(
        max_length=80,
        blank=True,
        null=True,
    )

    hotel_price = models.TextField(
        max_length=80,
        blank=True,
        null=True,
    )

    flight_price = models.TextField(
        max_length=80,
        blank=True,
        null=True,
    )

    location = models.TextField(
        max_length=120,
        blank=True,
        null=True,
    )

    country = models.TextField(
        max_length=120,
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    location_link = models.CharField(
        max_length=80,
        blank=True,
        null=True,
    )

    location_link_text = models.CharField(
        max_length=80,
        blank=True,
        null=True,
    )

    features = models.ManyToManyField(
        'destinations.Feature',
        related_name='+',
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        verbose_name = 'destination'
        verbose_name_plural = 'destinations'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.page.page.reverse('destination_detail', kwargs={
            'slug': self.slug
        })


class Feature(models.Model):

    title = models.CharField(
        max_length=255,
    )

    slug = models.SlugField(
        unique=True
    )

    feature_image = ImageRefField(
        verbose_name='Image',
        blank=False,
        null=True,
    )

    feature_description = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title


class DestinationImage(models.Model):
    destination = models.ForeignKey(
        'destinations.Destinations',
    )

    image = ImageRefField()

    def __str__(self):
        return f"{self.destination.title}'s image"
