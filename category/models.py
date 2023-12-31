from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=200)
    cat_image = models.ImageField(upload_to='photos/categories')

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name
