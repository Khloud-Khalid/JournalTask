from django.contrib import admin
from django.urls import include,path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', auth_views.LoginView.as_view(template_name='journal/login.html'), name='index'),
	url(r'^login/$', auth_views.LoginView.as_view(template_name='journal/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='journal/logout.html'), name='logout'),
    url(r'^admin/', admin.site.urls),
    path('journal/', include('journal.urls')),
]
