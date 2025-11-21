from django.db import models
import datetime
import os
from django.contrib.auth.models import User

# Create your models here.

def get_file_path(request,filename):
    original_filename = filename
    notTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (notTime,original_filename)
    return os.path.join('uploads/',filename)

class Category(models.Model):
    slug = models.CharField(max_length = 50, null = False, blank = False)
    name = models.CharField(max_length = 50, null = False, blank = False)
    image = models.ImageField(upload_to = get_file_path, null = False, blank = True)
    description = models.TextField(max_length = 100, null = False, blank = False)
    status = models.BooleanField(default = False, help_text = "0 = default, 1 = Hidden")
    trending = models.BooleanField(default = False, help_text = "0 = default, 1 = Trending")
    meta_title = models.CharField(max_length = 100, null = False, blank = False)
    meta_keyword = models.CharField(max_length = 40, null = False, blank = False)
    meta_description = models.CharField(max_length = 50, null = False, blank = False)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    slug = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=False, blank=True)
    small_description = models.CharField(max_length=50, null=False, blank=False)
    quantity = models.IntegerField(null = False, blank = False)
    description = models.TextField(max_length=100, null=False, blank=False)
    original_price = models.FloatField(null = False, blank = False)
    selling_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0 = default, 1 = Hidden")
    trending = models.BooleanField(default=False, help_text="0 = default, 1 = Trending")
    tag = models.CharField(max_length = 20, null = False, blank = False)
    meta_title = models.CharField(max_length=100, null=False, blank=False)
    meta_keyword = models.CharField(max_length=40, null=False, blank=False)
    meta_description = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    product_qty = models.IntegerField(null = False,blank = False)
    created_at = models.DateTimeField(auto_now_add = True)

class Wishlist(models. Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    fname = models.CharField(max_length = 20, null = False)
    lname = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length = 20, null = False)
    address = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=11, null=False)
    state = models.CharField(max_length=15, null=False)
    country = models.CharField(max_length=11, null=False)
    pincode = models.CharField(max_length=11, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=100, null=False)
    payment_id = models.CharField(max_length=20, null=False)

    orderstatus = {
        ("Pending","Pending"),
        ("Out of shipping","Out of shipping"),
        ("Completed","Completed"),
    }

    status = models.CharField(max_length = 100, choices = orderstatus,default = "pending")
    messages = models.TextField(null = False)
    tracking_no = models.CharField(max_length = 20,null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{} - {}'.format(self.id,self.tracking_no)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    price = models.FloatField(null = False)
    quantity = models.IntegerField(null = False)

    def __str__(self):
        #return '{} {}'.format(self.order.order.tracking_no)
        return f'Order: {self.order.tracking_no}, Product: {self.product}'

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    phone = models.CharField(max_length = 100, null = False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=100, null=False)
    pincode = models.CharField(max_length=20, null=False)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user.username
