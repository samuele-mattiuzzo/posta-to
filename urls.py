from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),

    ('^login/$', 'django.contrib.auth.views.login'),
    ('^logout/$', 'django.contrib.auth.views.logout'),

    #('^posts/P<year>\d+/P<month>\d+/P<day>\d+/P<title>\w+$', 'blog.views.view_post'),
    ('^posts/$', 'blog.views.view_all_posts'),
    ('^posts/new/$', 'blog.views.new_post'),

)
