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
    #('^users/(?P<id>\d+)/profile-page$', 'stats.views.profile_page'),
    #('^users/(?P<id>\d+)/charts$', 'stats.views.charts'),
    #('^blog/stats/$', 'stats.views.blog_stats'),

    ## post related pages ##
    ('^posts/$', 'blog.views.view_posts'),
    ('^posts/(?P<id>\d+)/$', 'blog.views.view_post'),
    ('^posts/new/$', 'blog.views.new_post'),
    ('^posts/delete/(?P<id>\d+)/$', 'blog.views.delete_post'),

    ## comment related urls (ajax) ##
    ('^comment/new/$', 'blog.views.new_comment'),
    #('^comment/delete/(?P<id>\d+)/$', 'blog.views.delete_comment'),
    ('^vote/(?P<id>\d+)/(?P<vote>\w+)/$', 'blog.views.vote_post'),
    #('^signup/$', 'blog.ajax.signup_user'),

)
