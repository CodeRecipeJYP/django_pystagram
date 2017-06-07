from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new/', views.new_photo),
    url(r'^(?P<photo_id>\d+)$', views.single_photo, name='view_single_photo'),
]