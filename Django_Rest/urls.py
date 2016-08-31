from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

from blog.views import blog_page, blog_api, schema_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'Django_Rest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest-api/', include('rest_framework.urls')),

    #blog
    url(r'^blog/', blog_page),

    #rest
    url(r'^api/blog',blog_api.as_view()),

    #swagger
    url(r'^swagger/', schema_view),


    #index
    url(r'^$', lambda r: HttpResponseRedirect('swagger/')),
]
