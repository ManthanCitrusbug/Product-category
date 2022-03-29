from distutils.command.upload import upload
from operator import truediv
from django.db import models
from django.contrib.auth.models import User ,AbstractUser
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    user = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100,blank=False)
    product_discription = models.TextField()
    product_image = models.ImageField(upload_to='image/',default="")
    product_price = models.PositiveIntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE,default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name


# class User(AbstractUser):
#     products = models.ForeignKey(AddProduct, on_delete=models.CASCADE, default="")
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")

#     def __str__(self):
#         return self.username