from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail import blocks
from modelcluster.fields import ParentalKey


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

    video = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('quote_text'),
        FieldPanel('quote_author'),
        FieldPanel('bio'),
        FieldPanel('image'),
        FieldPanel('image_caption'),
        InlinePanel('bandcamp_embeds', label="Bandcamp Embed"),
        InlinePanel('soundcloud_embeds', label="Soundcloud Embed"),
        FieldPanel('video'),
    ]

    @property
    def rendition_url(self):
        url = self.image.get_rendition('fill-800x800|jpegquality-60').url
        return url


class BandcampTracks(Orderable):
    page = ParentalKey(Epk,
                       on_delete=models.CASCADE,
                       related_name='bandcamp_embeds')
    title = models.CharField(max_length=50, default='')
    url = models.URLField()

    panels = [
        FieldPanel('title'),
        FieldPanel('url'),
    ]


class SoundcloudTracks(Orderable):
    page = ParentalKey(Epk,
                       on_delete=models.CASCADE,
                       related_name='soundcloud_embeds')
    title = models.CharField(max_length=50, default='')
    url = models.URLField()

    panels = [
        FieldPanel('title'),
        FieldPanel('url'),
    ]
