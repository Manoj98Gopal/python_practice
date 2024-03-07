from django.db import models

# Create your models here.

# creating model, here inheriting the modelsclass of Model method
class Product(models.Model):
    
    # creating fields and passing the parameters
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)
    
    
    
class Customer(models.Model):
    
    MEMBERSHI_BRONZE = 'B'
    MEMBERSHI_SILVER = 'S'
    MEMBERSHI_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHI_BRONZE,'bronze'),
        (MEMBERSHI_SILVER,'sliver'),
        (MEMBERSHI_GOLD,'gold')
    ]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_lenght=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null = True)
    # creating the choice fields and adding the default field
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES,default=MEMBERSHI_BRONZE)
    
    
    
class Order(models.Model):
    
    PAYMENT_PENDING = 'P'
    PAYMENT_FAILD = 'F'
    PAYMENT_SUCCESS = 'S'
    
    PAYMENT_CHOICES = [
        (PAYMENT_PENDING,'Pending'),
        (PAYMENT_FAILD,'Faild'),
        (PAYMENT_SUCCESS,'Success')
    ]
    
    place_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=PAYMENT_CHOICES,default=PAYMENT_PENDING)    