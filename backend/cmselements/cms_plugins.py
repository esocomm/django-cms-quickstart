from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from .models import (
    Header,
    Container,
    SectionHeading,
    SectionParagraph,
    Video,
)


@plugin_pool.register_plugin
class HeaderPlugin(CMSPluginBase):
    model = Header
    module = 'ELT'
    name = 'Header Plugin'
    render_template = "plugins/header_plugin.html"
    cache = False
    allow_children = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class ContainerPlugin(CMSPluginBase):
    model = Container
    module = 'ELT'
    name = 'Container Plugin'
    render_template = "plugins/container_plugin.html"
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class SectionHeadingPlugin(CMSPluginBase):
    model = SectionHeading
    module = 'ELT'
    name = 'Heading 1 Plugin'
    render_template = "plugins/sectionheading_plugin.html"
    cache = False
    allow_children = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class SectionParagraphPlugin(CMSPluginBase):
    model = SectionParagraph
    module = 'ELT'
    name = 'Paragraph Plugin'
    render_template = "plugins/sectionparagraph_plugin.html"
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class VideoPlugin(CMSPluginBase):
    model = Video
    module = 'ELT'
    name = 'Video Plugin'
    render_template = "plugins/video_plugin.html"
    cache = False
    allow_children = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

