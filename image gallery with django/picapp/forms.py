from .models import Photo, Album
from django import forms


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'image', 'tags', 'album']

    image = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        submitter = kwargs.pop('submitter')
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['album'].queryset = Album.objects.filter(
            submitter=submitter) | Album.objects.filter(is_public=True)


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['title', 'description', 'thumb', 'is_public']
        help_texts = {
            'is_public': ('(Uncheck for private album)')}
