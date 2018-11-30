from django.db import models
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    brand = models.CharField(max_length=50, default='')
    
   
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    
    def __str__(self):
        return self.name

class Review(models.Model):
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    title=models.CharField(max_length=254, default='')
    content=models.TextField()
    product=models.ForeignKey(Product, null=False, default=1, related_name='reviews', on_delete=models.CASCADE)