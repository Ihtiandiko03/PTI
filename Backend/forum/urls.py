from django.conf.urls import url

from . import views
from .models import komentar

urlpatterns = [
	# url(r'^update/(?P<update_id>[0-9]+)$', views.update, name='update'),
	# url(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
	url(r'^create/$', views.create),
	url(r'^$', views.index, name='list'),
	url(r'^post/(?P<slugInput>[\w-]+)/$', views.isi_berita),
	url(r'^comment/(?P<id_topik>[\w-]+)/$', views.buat_komentar),
	url(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
	url(r'^update/(?P<update_id>[0-9]+)$', views.update, name='update'),
	# url(r'^posts/(?P<slugInput>[\w-]+)/$', views.singlePost),
	# url(r'^event/', views.event),
]