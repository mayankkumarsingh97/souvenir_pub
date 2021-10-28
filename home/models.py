from django.db import models
from django.forms import ModelForm
from embed_video.fields import EmbedVideoField

# Create your models here.
class VideoLink(models.Model):
    video = EmbedVideoField()
    video_name = models.CharField(max_length=100, blank=True)

    # def __str__:
    #     return self.video_name


class customersupportmodel(models.Model):
    # first_name = models.CharField(max_length=200, blank=True, verbose_name=' First Name')
    # last_name = models.CharField(max_length=200, blank=True, verbose_name=' Last Name')
    email = models.CharField(max_length=200, blank=True, verbose_name='Email')
    # phone = models.CharField(max_length=200, blank=True, verbose_name='Phone')
    # message = models.CharField(max_length=200, blank=True, verbose_name='Message')


class catalog(models.Model):
    # first_name = models.CharField(max_length=200, blank=True, verbose_name=' First Name')
    # last_name = models.CharField(max_length=200, blank=True, verbose_name=' Last Name')
    file = models.FileField(upload_to=None)
    latest_catalog=models.CharField(max_length=200, blank=True, verbose_name='Latest Catlog')
    # phone = models.CharField(max_length=200, blank=True, verbose_name='Phone')
    # message = models.CharField(max_length=200, blank=True, verbose_name='Message')

    def __str__(self):
        return f'{self.latest_catalog}'

class contactUsForm(ModelForm):
    class Meta:
        model = customersupportmodel
        fields = [ 'email']
