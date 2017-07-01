from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^roles/(?P<pk>[0-9]+)/$', views.RoleDetailView.as_view(), name='role_detail'),
    url(r'^setups/(?P<pk>[0-9]+)/$', views.SetupDetailView.as_view(), name='setup_detail'),
]