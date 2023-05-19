from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from .models import Header


@plugin_pool.register_plugin
class HeaderPlugin(CMSPluginBase):
    model = Header
    name = 'Header Plugin'
    render_template = "plugins/header_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

