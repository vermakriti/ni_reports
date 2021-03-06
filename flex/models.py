from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from streams import blocks

# Create your models here.
class FlexPage(Page):

    template = "flex/flex_page.html"
    content_title = models.CharField(max_length=100, null=True, blank=True)
    content_subtitle =  models.CharField(max_length=500,blank=True,null=True)
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
        ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("content_title"),
        FieldPanel("content_subtitle"),
        StreamFieldPanel("content"),
    ]

    class Meta:  # noqa 
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"