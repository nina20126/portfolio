from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from autoslug import AutoSlugField
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail
from django.core.exceptions import ValidationError
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


class Album(models.Model):

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" %
                                  str(megabyte_limit))

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    submitter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True, verbose_name="Public Album")
    slug = AutoSlugField(populate_from='title', unique=True)
    thumb = ProcessedImageField(upload_to='photos/', processors=[Thumbnail(
        400, 400)], format='JPEG', options={'quality': 90}, validators=[validate_image])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photos', kwargs={'slug': self.slug})


class Photo(models.Model):

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" %
                                  str(megabyte_limit))

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    image = ProcessedImageField(upload_to='photos/',
                                processors=[ResizeToFit(
                                    width=1024, upscale=False)],
                                format='JPEG',
                                options={'quality': 90},
                                validators=[validate_image])
    image_medium = ImageSpecField(source='image',
                                  processors=[Thumbnail(400, 400,)],
                                  format='JPEG',
                                  options={'quality': 90})
    submitter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('images', kwargs={'id': self.pk})

    def save(self, *args, **kwargs):
        self.is_public = Album.objects.get(title=self.album).is_public
        super().save(*args, **kwargs)
