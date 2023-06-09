from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class PressReleaseApphook(CMSApp):
    app_name = "release"
    name = "Press Release Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["backend.release.urls"]


@apphook_pool.register
class MediaApphook(CMSApp):
    app_name = "backend.esomedia"
    name = "ESO Media Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["backend.esomedia.urls"]

