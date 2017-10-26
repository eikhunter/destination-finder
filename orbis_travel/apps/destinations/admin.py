from cms.admin import PageBaseAdmin
from django.contrib import admin

from .models import Destination, Feature


@admin.register(Destination)
class DestinationAdmin(PageBaseAdmin):
    fieldsets = [
        (None, {
            'fields': ['page', 'title', 'slug'],
        }),
        ('Basics', {
            'fields': ['weather', 'flight_price', 'hotel_price', 'image'],
        }),
        ('Details', {
            'fields': ['location', 'country', 'description', 'location_link', 'location_link_text'],
        }),
        PageBaseAdmin.PUBLICATION_FIELDS,
        PageBaseAdmin.NAVIGATION_FIELDS,
        PageBaseAdmin.SEO_FIELDS,
        PageBaseAdmin.OPENGRAPH_FIELDS,
        PageBaseAdmin.OPENGRAPH_TWITTER_FIELDS
    ]

    filter_horizontal = ['features']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
