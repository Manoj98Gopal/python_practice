from django.db import models

# Create your models here.

# creating model, here inheriting the modelsclass of Model method


class Collection(models.Model):
    
    title = models.CharField(max_length=255)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name="products_in_collection")
    
    
class Promotions(models.Model):
    
    discription = models.CharField(max_length=255)
    discount = models.FloatField()




class Product(models.Model):
    
    # creating fields and passing the parameters
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name="products")
    promotion = models.ManyToManyField(Promotions)
    
    
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
    last_name = models.CharField(max_length=255)
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
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    

class OrderItem(models.Model):
    
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)    
    quantity = models.PositiveSmallIntegerField()
    unitprice = models.DecimalField(max_digits=6,decimal_places=2)
    
class Address(models.Model):
    
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    zip = models.CharField(null=False,max_length=20)
    
    
class Cart(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class CartItem(models.Model):
    
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()