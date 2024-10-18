from django import forms

from petstagram.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'location': forms.TextInput(attrs={'value': 'Location'}),
        }








    # 33 благоев болница - неделя камерната зала
    # 13 часа обучение