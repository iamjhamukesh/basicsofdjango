#will contain just the urls of my music compartment
from django.conf.urls import url
from . import views #. is for current directory's views

app_name="music"


urlpatterns = [
    # /music/
    url(r'^$',views.IndexView.as_view(),name='index'), #default section in music

    #/music/71<album_id>/            (ID)(details waala tab)
    url(r'^(?P<pk>[0-9]+)/$',views.DetailsView.as_view(),name="detail"), #keyword used in index

    # /music/71<album_id>/favourite
    #url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favorite, name="favorite"),  # keyword used in index

    #music/album/add/
    url(r'album/add/$',views.AlbumCreate.as_view(),name="album-add"),

    #music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name="album-update"),

    #music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name="album-delete"),

]

