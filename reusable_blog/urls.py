from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.blog_posts, name='blog_posts'),
    url(r'^blog/$', views.blog_posts, name='blog_posts'),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.edit_post, name='edit_post'),

]