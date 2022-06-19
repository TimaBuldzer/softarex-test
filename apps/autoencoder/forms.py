from django import forms
from django.core.files.images import ImageFile

from apps.autoencoder.autoencoder import Autoencoder
from apps.autoencoder.models import Case


class CreateCaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['original']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateCaseForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        case = Case.objects.create(
            user=self.request.user,
            original=self.cleaned_data['original']
        )
        autoencoder = Autoencoder()
        encoded = autoencoder.predict(case.original.name)
        image = ImageFile(encoded, name='encoded.jpg')
        case.encoded = image
        case.save(update_fields=['encoded'])
        return case
