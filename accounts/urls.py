from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
	url(r'^login/$', login, name='login', kwargs={
		'template_name': 'accounts/login_form.html',
	}),
	url(r'^signup/$', views.signup, name='signup'),
]
