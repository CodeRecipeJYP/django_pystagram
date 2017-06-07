# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views  # 이 줄 추가.

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'pystagram.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin[a-z0-9]/', include(admin.site.urls)),

    url(r'^photos/', include('photos.urls')),

    url(r'^users/', include('profiles.urls')),

    url(
        r'^accounts/login/', auth_views.login, name='login',
        kwargs={
            'template_name': 'login.html'
        }
    ),
    url(
        r'^accounts/logout/', auth_views.logout, name='logout',
        kwargs={
            'next_page': settings.LOGIN_URL,
        }
    ),

    url('', include('social.apps.django_app.urls', namespace='social')),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )