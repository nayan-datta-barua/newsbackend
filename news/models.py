from django.db import models
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
import uuid
User = settings.AUTH_USER_MODEL
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=30)
    keywords = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    # image = models.ImageField(blank=True, upload_to='images/')
    slug = models.SlugField(unique=True,default=uuid.uuid1,allow_unicode=True,)
    parent = models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE,related_name='children')
    timestamp = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Category, self).save(*args, **kwargs)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if not self.slug:
            slug_str = f"{self.name}"
            self.slug = slugify(slug_str, allow_unicode=True)
            super(Category, self).save(*args, **kwargs)


    def __str__(self):
        return self.name


class News(models.Model):
    # author = models.ForeignKey(
    #     Author, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=250, blank=False)
    slug = models.SlugField(unique=True,default=uuid.uuid1,allow_unicode=True,)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')
    thumbnail_url = models.URLField(max_length=300, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # ratings = GenericRelation(Rating, related_query_name='ratings')
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')
    # tags = TaggableManager()
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if not self.slug:
            slug_str = f"{self.title}"
            self.slug = slugify(slug_str, allow_unicode=True)
            super(News, self).save(*args, **kwargs)
            
    def _str_(self):
        return self.title
    
    
