from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^update/(?P<update_id>[0-9]+)$', views.update, name='update'),
	url(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
	url(r'^create/$', views.create, name='create'),
	url(r'^$', views.index, name='list'),
	url(r'^posts/(?P<slugInput>[\w-]+)/$', views.singlePost),
	url(r'^event/', views.event),
]