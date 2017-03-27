from django.conf.urls import url
from . import views

app_name = 'savaan'

urlpatterns = [
    # savaan/
    url(r'^$', views.index, name='index'),

    # savaan/id/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # savaan/id/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]

