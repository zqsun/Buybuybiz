from django.conf.urls import include,url

from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^login/$', auth_views.login,  {'template_name': 'account/registration/login.html'},name='login'),
	url(r'^logout/$', auth_views.logout,name='logout'),
	# url('', include('django.contrib.auth.urls')),
	# url(r'^transit$', views.transit, name='transit'),
	# url(r'^(?P<kw>[\w|\W]+)/(?P<cat>[\w|\W]+)/listing$', views.listing, name='listing'),
	# url(r'^(?P<cat>[\w|\W]+)/(?P<kw>[\w|\W]+)/listing$', views.listing, name='listing'),

]