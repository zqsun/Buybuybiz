from django.forms import ModelForm
from myaccount.models import Product,productPic

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ['name','description','price','quantity','category']

class productPicform(ModelForm):
	class Meta:
		model = productPic
		fields = ['picture']
			
		