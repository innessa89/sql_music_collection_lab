import pdb
from typing import AsyncIterable
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository




# artist_repository.select_all()

# albums= album_repository.select_all()
# for album in albums:
#     print(album.__dict__)




# artist1=Artist("Adele")
# artist_repository.save(artist1)
# artist2=Artist("JLO")
# artist_repository.save(artist2)

# album=Album("New album",artist1,"pop")
# album_repository.save(album)

# albums= album_repository.select_all()
# for album in albums:
#     print(album.__dict__)

artist=Artist("Adele")
saved_artist = artist_repository.save(artist)

album=Album("Adeles album",saved_artist,"pop")
album_repository.save(album)
album2=Album("Adeles 2nd album",saved_artist,"pop")
album_repository.save(album2)

albums = album_repository.select_all_by_artist(saved_artist)

for album in albums:
    print(album.__dict__)


pdb.set_trace()    