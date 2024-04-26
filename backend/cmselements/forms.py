from backend.utils.models import Category
from django import forms
from django.forms import inlineformset_factory

from backend.utils.models import Category, Tag
from backend.esomedia.models import Image, ImageInAFormat, ImageFormat


class TagWizardForm(forms.Form):

    slug = forms.SlugField()
    name = forms.CharField()


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

class ImageInAFormatWizardForm(forms.Form):

    image = forms.ModelChoiceField(queryset=Image.objects.all(), widget=forms.widgets.TextInput())
    format = forms.ModelChoiceField(queryset=ImageFormat.objects.all())
    # This should be a FilerImageField()
    # Or Image should be an extension of Django-Filer? Not enough for our needs probably
    image_file = forms.FileField()


