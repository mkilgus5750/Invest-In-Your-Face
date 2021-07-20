from django.db import models
from django.db import models
from oauth2client.contrib.django_util.models import CredentialsField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Store(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    purchase_options = models.ManyToManyField(Store)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='products', null=True)
    slug = models.SlugField(db_index=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    blurb = models.CharField(max_length=300)
    image = models.ImageField(upload_to='posts', null=True)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.title