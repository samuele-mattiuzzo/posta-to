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

    ## stats related pages ##
    ('^users/(?P<id>\d+)/(?P<username>\w+)$', 'users.views.profile'),
    ('^users/(?P<id>\d+)/(?P<username>\w+)/charts/$', 'users.views.charts'),
    ('^signup/$', 'users.views.signup'),

    ## post related pages ##
    ('^posts/$', 'blog.views.view_posts'),
    ('^posts/(?P<id>\d+)/$', 'blog.views.view_post'),
    ('^posts/new/$', 'blog.views.new_post'),
    ('^posts/delete/(?P<id>\d+)/$', 'blog.views.delete_post'),
    ('^top/$', 'blog.views.view_top_ranked'),

    ## image serving ##
    ('^posts/download/(?P<id>\d+)/$', 'blog.views.download_handler'),

    ## comment related urls (ajax) ##
    ('^comment/new/$', 'blog.ajax.new_comment'),
    ('^vote/(?P<id>\d+)/(?P<vote>\w+)/$', 'blog.ajax.vote_post'),

)
