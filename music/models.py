from django.db import models
from django.urls import reverse
#contains blueprint
#ID 1 for below class
class Album(models.Model):
    #artist is basically a column in db
    artist = models.CharField(max_length=250) #artist name is character for 250 lengths
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.CharField(max_length=1000)

    def get_absolue_urll(self):
       return reverse("music:detail",kwargs={'pk':self.pk}) #music/2

    #type all the details inside the interactive shell
    def __str__(self):#string representation of album
        return self.album_title +"-"+ self.artist
#Id 2
class Song(models.Model):
    #ForeignKey is basically a id here it is 1
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    is_favorite =models.BooleanField(default=False)
    def __str__(self):#string representation of album
        return self.song_title

