from django.db import models
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    post_at = models.DateTimeField(auto_now=True)
    title   = models.CharField(max_length=50)
    description = models.CharField(max_length=150,default = '')
    content = RichTextUploadingField(blank=True)
    
    def __str__(self):
        return f'{self.title}'
