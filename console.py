import pdb
from typing import AsyncIterable
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository




artist_repository.select_all()

albums= album_repository.select_all()
for album in albums:
    print(album.__dict__)





pdb.set_trace()    