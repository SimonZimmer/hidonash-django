from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class Epk(Page):
    quote_text = RichTextField(blank=True)
    quote_author = RichTextField(blank=True)
    bio = RichTextField(blank=True)
    image = models.ForeignKey(
            "wagtailimages.Image",
            null=True,
            blank=False,
            on_delete=models.SET_NULL,
            related_name="+",
        )
    image_caption = models.CharField(max_length=50, blank=True)
    spotlight_track_1 = models.URLField(blank=True)
    spotlight_track_2 = models.URLField(blank=True)
    spotlight_track_3 = models.URLField(blank=True)

    spotlight_mix_1 = models.URLField(blank=True)
    spotlight_mix_2 = models.URLField(blank=True)

    video = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('quote_text'),
        FieldPanel('quote_author'),
        FieldPanel('bio'),
        FieldPanel('image'),
        FieldPanel('image_caption'),
        FieldPanel('spotlight_track_1'),
        FieldPanel('spotlight_track_2'),
        FieldPanel('spotlight_track_3'),
        FieldPanel('spotlight_mix_1'),
        FieldPanel('spotlight_mix_2'),
        FieldPanel('video'),
    ]

    @property
    def rendition_url(self):
        url = self.image.get_rendition('fill-800x500|jpegquality-60').url
        return url
