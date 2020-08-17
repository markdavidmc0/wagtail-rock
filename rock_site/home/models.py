from django.db import models  # noqa: F401

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    pass


class MediaPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('carousel', blocks.StreamBlock([
            ('first_image', ImageChooserBlock()),
            ('second_image', ImageChooserBlock()),
            ('third_image', ImageChooserBlock()),
            ('fourth_image', ImageChooserBlock()),
            ('fifth_image', ImageChooserBlock()),
        ], icon='cogs'
        )),
        ('switcher', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('description', blocks.RichTextBlock()),
        ], icon='user'))

    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
