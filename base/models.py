from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.timezone import now
import datetime
from django.urls import reverse
# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name




class Posts(models.Model):
    headline =  models.CharField(max_length=300)
    Sub_headline = models.CharField(max_length=300, null = True, blank=True)
    
    thumbnail = models.ImageField(null=True, blank=True, upload_to ="images", default="placeholder.jpg")
    body = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    publish = models.BooleanField(default = False)
    featured = models.BooleanField(default = False)
    tags = models.ManyToManyField(Tags, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    

    def __str__(self):
        return self.headline
    def get_absolute_url(self):
        return reverse('article', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.headline)

            has_slug = Posts.objects.filter(slug=slug).exists()
            count=1
            while has_slug:
                count +=1
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Posts.objects.filter(slug=slug).exists()
            self.slug = slug
       

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        #self.body.delete()
        self.thumbnail.delete()
        super().delete(*args, **kwargs)

