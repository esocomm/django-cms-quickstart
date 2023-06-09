from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from .forms import ImageWizardForm
from backend.esomedia.models import Image, Video

class MediaWizard(Wizard):
    pass

image_wizard = MediaWizard(
    title="New Image",
    weight=200,
    form=ImageWizardForm,
    model=Image,
    description="Create a new Image instance",
)

wizard_pool.register(image_wizard)

