from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
     url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
     url(r'^post/new/$', views.post_new, name='post_new'), 
     url(r'^family/new/$', views.family_new, name='family_new'),
    # url(r'^family/$',  views.search_new, name='search_new'), 
     url(r'^$',  views.search_new, name='search_new'),    
     url(r'^family/(?P<pk>[0-9]+)/$', views.post_detail, name='family_detail'),
]