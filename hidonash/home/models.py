from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class Epk(Page):
    quote = RichTextField(blank=True)
    bio = RichTextField(blank=True)
    image = models.ForeignKey(
            "wagtailimages.Image",
            null=True,
            blank=False,
            on_delete=models.SET_NULL,
            related_name="+",
        )
    spotlight_track_1 = models.URLField(blank=True)
    spotlight_track_2 = models.URLField(blank=True)
    spotlight_track_3 = models.URLField(blank=True)

    spotlight_mix_1 = models.URLField(blank=True)
    spotlight_mix_2 = models.URLField(blank=True)

    video = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('quote'),
        FieldPanel('bio'),
        FieldPanel('image'),
        FieldPanel('spotlight_track_1'),
        FieldPanel('spotlight_track_2'),
        FieldPanel('spotlight_track_3'),
        FieldPanel('spotlight_mix_1'),
        FieldPanel('spotlight_mix_2'),
        FieldPanel('video')
    ]

    @property
    def rendition_url(self):
        url = self.image.get_rendition('fill-800x500|jpegquality-60').url
        return url
