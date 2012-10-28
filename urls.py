from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'blog.views.view_posts'),
    ('^about/$', 'django.views.generic.simple.direct_to_template', {'template': 'about.html'}),


    ('^login/$', 'django.contrib.auth.views.login'),
    ('^logout/$', 'django.contrib.auth.views.logout'),

    ('^posts/$', 'blog.views.view_posts'),
    ('^posts/(?P<id>\d+)/$', 'blog.views.view_posts'),
    ('^posts/new/$', 'blog.views.new_post'),

)
