"""palestra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^$', 'tchelinux2015.views.inicial'),
    url(r'^slide2/', 'tchelinux2015.views.slide2'),
    url(r'^slide3/', 'tchelinux2015.views.slide3'),
    url(r'^slide4/', 'tchelinux2015.views.slide4'),
    url(r'^slide5/', 'tchelinux2015.views.slide5'),
    url(r'^slide6/', 'tchelinux2015.views.slide6'),
    url(r'^slide7/', 'tchelinux2015.views.slide7'),
    url(r'^slide8/', 'tchelinux2015.views.slide8'),
    url(r'^slide9/', 'tchelinux2015.views.slide9'),

#    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
        urlpatterns += patterns('',
                (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
        )
                
