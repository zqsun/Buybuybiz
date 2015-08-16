from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add/$',views.addProduct, name='addproduct'),
	url(r'^myproducts/$',views.myProducts, name='myproducts'),
	url(r'^edit/(?P<product_id>[0-9]+)/$',views.editProduct, name='editProduct'),
	url(r'^delete/(?P<product_id>[0-9]+)/$',views.delProduct, name='delProduct'),
	# url(r'^(?P<question_id>[0-9]+)/$',views.details,name='details'),
	# url(r'^login/$', auth_views.login,  {'template_name': 'account/registration/login.html'},name='login'),
	# url('', include('django.contrib.auth.urls')),
	# url(r'^transit$', views.transit, name='transit'),
	# url(r'^(?P<kw>[\w|\W]+)/(?P<cat>[\w|\W]+)/listing$', views.listing, name='listing'),
	# url(r'^(?P<cat>[\w|\W]+)/(?P<kw>[\w|\W]+)/listing$', views.listing, name='listing'),

]