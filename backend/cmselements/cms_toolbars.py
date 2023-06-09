from cms.utils.urlutils import admin_reverse
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from backend.release.models import PressRelease


class PressReleaseToolbar(CMSToolbar):
    supported_apps = ['release']

    def populate(self):

        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu('release_cms_integration-pressrelease', 'Press Release')

        menu.add_sideframe_item(
            name='Press Release list',
            url=admin_reverse('release_pressrelease_changelist'),
        )

        menu.add_modal_item(
            name=('Add a new Press Release'),
            url=admin_reverse('release_pressrelease_add'),
        )

        # buttonlist = self.toolbar.add_button_list()
        #
        # buttonlist.add_sideframe_button(
        #     name='Press Release list',
        #     url=admin_reverse('release_pressrelease_changelist'),
        # )
        #
        # buttonlist.add_modal_button(
        #     name='Add a new Press Release',
        #     url=admin_reverse('release_pressrelease_add'),
        # )


class MediaToolbar(CMSToolbar):
    supported_apps = ['backend.esomedia']

    def populate(self):

        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu('esomedia_cms_integration-esomedia', 'Media')

        menu.add_sideframe_item(
            name='Image list',
            url=admin_reverse('esomedia_image_changelist'),
        )

        menu.add_modal_item(
            name=('Add a new Image'),
            url=admin_reverse('esomedia_image_add'),
        )

        menu.add_sideframe_item(
            name='Video list',
            url=admin_reverse('esomedia_video_changelist'),
        )

        menu.add_modal_item(
            name=('Add a new Video'),
            url=admin_reverse('esomedia_video_add'),
        )

        # buttonlist = self.toolbar.add_button_list()
        #
        # buttonlist.add_sideframe_button(
        #     name='Image list',
        #     url=admin_reverse('esomedia_image_changelist'),
        # )
        #
        # buttonlist.add_modal_button(
        #     name='Add a new Image',
        #     url=admin_reverse('esomedia_image_add'),
        # )
        #
        # buttonlist.add_sideframe_button(
        #     name='Video list',
        #     url=admin_reverse('esomedia_video_changelist'),
        # )
        #
        # buttonlist.add_modal_button(
        #     name='Add a new video',
        #     url=admin_reverse('esomedia_video_add'),
        # )

toolbar_pool.register(PressReleaseToolbar)  # register the toolbar
toolbar_pool.register(MediaToolbar)  # register the toolbar

