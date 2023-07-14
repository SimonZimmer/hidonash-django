from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class Epk(Page):
    bio = RichTextField(blank=True)
    image = models.ForeignKey(
            "wagtailimages.Image",
            null=True,
            blank=False,
            on_delete=models.SET_NULL,
            related_name="+",
        )

    content_panels = Page.content_panels + [
        FieldPanel('bio'),
        FieldPanel('image')
    ]

    @property
    def rendition_url(self):
        url = self.image.get_rendition('fill-800x800|jpegquality-60').url
        return url
