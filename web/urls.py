from django.conf.urls import url, include
from django.contrib import admin
import views
from django.contrib.auth import views as auth_views

urlpatterns = [ 

url(r'^$',views.home, name='home'),
url(r'^about-us$',views.aboutus, name='aboutus'),
url(r'^user-login/$',auth_views.LoginView.as_view(template_name='Neels cafe/login.html',
    	extra_context={
    	'title' :'User Login',
    	'next' : '/about-us',
    	'login_url':'user_login'

    	}),name='user_login'),
url(r'^logout/$',auth_views.logout, {'next_page': '/'},name='logout'),
	
url(r'^contact-us',views.contact_us, name='contact_us'),

]