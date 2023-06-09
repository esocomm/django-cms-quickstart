from backend.utils.models import Category
from django import forms
from django.forms import inlineformset_factory

from backend.utils.models import Category, Tag
from backend.esomedia.models import Image, ImageInAFormat


class ImageWizardForm(forms.Form):

    slug = forms.SlugField()
    name = forms.CharField()
    published = forms.BooleanField()
    publication_datetime = forms.DateTimeField(widget=forms.SplitDateTimeWidget(
        date_attrs={'type': 'date', 'class': 'datepicker'},
        time_attrs={'type': 'time', 'class': 'timepicker'},
    ))
    embargo_datetime = forms.DateTimeField(widget=forms.SplitDateTimeWidget(
        date_attrs={'type': 'date', 'class': 'datepicker'},
        time_attrs={'type': 'time', 'class': 'timepicker'},
    ))
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    credit = forms.CharField(widget=forms.Textarea())
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())


# TODO Develop an import Feature to import and create derivatives, and link them to the image
class ImageInAFormatForm(forms.Form):

    class Meta:
        model = ImageInAFormat
        fields = '__all__'
    # image = models.ForeignKey(Image, on_delete=models.CASCADE)
    # format = models.ForeignKey(ImageFormat, on_delete=models.SET_NULL, null=True)
    # image_file = FilerImageField(on_delete=models.SET_NULL, null=True)


ImageInAFormatFormSet = inlineformset_factory(
    Image, ImageInAFormat, form=ImageInAFormatForm,
    extra=1, can_delete=True, can_delete_extra=True
)

