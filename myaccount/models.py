from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userData(models.Model):
	user = models.OneToOneField(User)
	sales = models.DecimalField(max_digits=11,decimal_places=2,default=0)
	orderNum = models.IntegerField(default=0)

class productCategory(models.Model):
	category = models.CharField(max_length=250,unique=True)
	# desc_chs = models.CharField(max_length=250)
	def __unicode__(self):
		return self.category

class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	quantity = models.DecimalField(max_digits=11,decimal_places=2)
	price = models.DecimalField(max_digits=11,decimal_places=2,default=0)
	sold_by = models.ForeignKey(User)
	category = models.ForeignKey(productCategory)
	def __unicode__(self):
		return self.name

class productPic(models.Model):
	product = models.ForeignKey(Product)
	picture = models.ImageField(upload_to='product_images',blank=True)
		

class orderStatus(models.Model):
	status = models.CharField(max_length=200,unique=True)
	def __unicode__(self):
		return self.status

class Order(models.Model):
	# sold_by = models.ForeignKey(User)
	bought_by = models.CharField(max_length=150)	
	status = models.ForeignKey(orderStatus)
	quantity = models.DecimalField(max_digits=11,decimal_places=2)
	orderDate = models.DateTimeField(auto_now_add=True)
	product = models.ForeignKey(Product)
	def __unicode__(self):
		return self.status
