from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myaccount.models import userData, productCategory, Product, productPic,orderStatus, Order
from myaccount.forms import ProductForm, productPicform
from django.contrib import messages

import os
from django.conf import settings

# Create your views here.
@login_required
def index(request):
	productsCount = Product.objects.filter(sold_by=request.user).count()
	context = {'productsCount': productsCount}
	return render(request, 'myaccount/index.html', context)
    # return HttpResponse("Hello, world. You're at the polls index.")

@login_required
def addProduct(request):
	tflag = "add"
	# print request.user.id
	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	# added = False
	
	if request.method == 'POST':
		product_form = ProductForm(request.POST)
		pic_form = productPicform(request.POST)
		if product_form.is_valid() :
			product = product_form.save(commit=False)
			product.sold_by = request.user
			product.save()
			# added = True
			# message = "Product: "+product.name+" is added successfullly."
			messages.success(request, 'Product: %s is successfullly added.' % product.name)

		if pic_form.is_valid():
			if 'picture' in request.FILES:
				pic = pic_form.save(commit=False)
				pic.product = product
				pic.picture = request.FILES['picture']
				pic.save()
		return HttpResponseRedirect(reverse('myaccount:myproducts'))
	else:
		product_form = ProductForm()
		pic_form = productPicform()

	context = {'product_form':product_form,'pic_form':pic_form}
	return render(request, 'myaccount/addproduct.html', context)
	# return HttpResponse("Hello, world. You're at the Add product.")

@login_required
def editProduct(request,product_id):
	tflag = "edit"
	# print request.user.id
	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	# added = False
	p = Product.objects.get(pk=product_id)
	try:
		pic_pre = productPic.objects.get(product = p)
	except productPic.DoesNotExist:
		pic_pre = None
	if p.sold_by != request.user:
		return HttpResponse("You don't have permission")
	if request.method == 'POST':
		product_form = ProductForm(request.POST,instance=p)
		pic_form = productPicform(request.POST,instance=pic_pre)
		if product_form.is_valid():
			product = product_form.save(commit=False)
			product.sold_by = request.user
			product.save()
			# added = True
			messages.success(request, 'Product: %s is successfullly updated.' % product.name)

		if pic_form.is_valid():
			pic_new = pic_form.save(commit=False)
			pic_new.product = product
			if 'picture' in request.FILES:
				# Delete the old picture
				if pic_pre:
					os.remove(os.path.join(settings.MEDIA_ROOT,pic_pre.picture.name))
				pic_new.picture = request.FILES['picture']
				pic_new.save()

		return HttpResponseRedirect(reverse('myaccount:myproducts'))
	else:
		product_form = ProductForm(instance=p)
		pic_form = productPicform(instance=pic_pre)
	context = {'product_form':product_form,'pic_form':pic_form,'tflag':tflag, 'product_id':product_id}
	return render(request, 'myaccount/addproduct.html', context)
	# return HttpResponse("Hello, world. You're at the Add product.")

def delProduct(request,product_id):
	product = Product.objects.get(pk=product_id)
	try:
		pic = productPic.objects.get(product = product)
	except productPic.DoesNotExist:
		pic = None
	# pic = productPic.objects.get(product = product)
	if product.sold_by != request.user:
		return HttpResponse("You don't have permission")
	else:
		if pic:
			os.remove(os.path.join(settings.MEDIA_ROOT,pic.picture.name))
			pic.delete()
		messages.success(request, 'Product: %s is successfullly deleted.' % product.name)
		product.delete()
		return HttpResponseRedirect(reverse('myaccount:myproducts'))

@login_required
def myProducts(request):
	products = Product.objects.filter(sold_by=request.user)
	# paginator = Paginator(products,5)
	# page = request.GET.get('page')
	# try:
	# 	li = paginator.page(page)
	# except PageNotAnInteger:
	# 	li = paginator.page(1)
	# except EmptyPage:
	# 	li = paginator.page(paginator.num_pages)
	# context = {'listings':li}
	context = {'listings':products}
	return render(request, 'myaccount/myproducts.html', context)
	# return HttpResponse("Hello, world. You're at the polls index.")
