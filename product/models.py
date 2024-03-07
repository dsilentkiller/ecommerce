from django.db import models

# Create your models here.


class ProductManager(models.Manager):
    def category(self, category_name):
        return self.get_queryset().filter(category_name=category_name)

    def get_queryset(self):
        return super().get_queryset().filter(price__gt=200)


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    summer_coll = models.CharField(max_length=200)
    autmon_coll = models.CharField(max_length=200)
    # inventary=models.ForeignKey
    hot_sell = models.CharField(max_length=200)
    discount = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='media/image', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    custom_objects = ProductManager()

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=300)
    discount = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __Str__(self):
        return self.name
