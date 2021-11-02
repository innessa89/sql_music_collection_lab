import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

albums= album_repository.select_all()
for album in albums:
    print(album.__dict__)