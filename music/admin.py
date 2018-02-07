from django.contrib import admin

from . models import Album,Song #make it appear in admin page for viewing

admin.site.register(Album)
admin.site.register(Song)
'''
<ul>
    {% for song in album.song_set.all %}
        <li>{{ song.song_title }}              {{ song.file_type}}</li>
    {% endfor %}
</ul>

'''