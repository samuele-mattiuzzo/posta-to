from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),

    ## homepage ##
    ('^$', 'blog.views.view_posts'),

    ## about page ##
    ('^about/$', 'django.views.generic.simple.direct_to_template', {'template': 'about.html'}),

    ## login/logout/signup pages ##
    ('^login/$', 'django.contrib.auth.views.login'),
    ('^logout/$', 'django.contrib.auth.views.logout'),

    ## post related pages ##
    ('^posts/$', 'blog.views.view_posts'),
    ('^posts/(?P<id>\d+)/$', 'blog.views.view_post'),
    ('^posts/new/$', 'blog.views.new_post'),

    ## ajax views ##
    ('^comment/new/$', 'blog.views.new_comment'),
    #('^posts/(?P<id>\d+)/promote/$', 'blog.views.promote_post'),
    #('^posts/(?P<id>\d+)/demote/$', 'blog.views.demote_post'),

)
