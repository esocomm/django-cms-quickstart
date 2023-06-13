from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from .forms import ImageWizardForm, TagWizardForm, ImageInAFormatWizardForm
from backend.esomedia.models import Image, Video, ImageInAFormat
from backend.utils.models import Tag, Category


class ImageWizard(Wizard):
    pass


class ImageInAFormatWizard(Wizard):
    pass


class TagWizard(Wizard):
    pass


class CategoryWizard(Wizard):
    pass


tag_wizard = TagWizard(
    title="New Tag",
    weight=200,
    form=TagWizardForm,
    model=Tag,
    description="Create a new Tag instance",
)

category_wizard = CategoryWizard(
    title="New Category",
    weight=200,
    form=TagWizardForm,
    model=Category,
    description="Create a new Category instance",
)

image_wizard = ImageWizard(
    title="New Image",
    weight=200,
    form=ImageWizardForm,
    model=Image,
    description="Create a new Image instance",
)

imageinaformat_wizard = ImageInAFormatWizard(
    title="New Image In A Format",
    weight=200,
    form=ImageInAFormatWizardForm,
    model=ImageInAFormat,
    description="Create a new Image In A Format instance",
)


wizard_pool.register(image_wizard)
wizard_pool.register(imageinaformat_wizard)
wizard_pool.register(tag_wizard)
wizard_pool.register(category_wizard)

