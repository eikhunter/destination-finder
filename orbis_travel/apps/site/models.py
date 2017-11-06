from cms.apps.pages.models import ContentBase


class Landing(ContentBase):

    urlconf = 'orbis_travel.apps.site.urls'

    def __str__(self):
        return self.page.title
