from db.run_sql import run_sql

from models.album import Album
from repositories import artist_repository

def select_all():  
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist=artist_repository.select(row["artist_id"])
        album = Album(
            row['title'],
            artist,
            row['genre'],
            row['id'] 
            )
        albums.append(album)
    return albums

# def save(task):
#     sql="INSERT INTO tasks (description, user_id, duration, completed) VALUES (%s,%s,%s,%s) RETURNING *"
#     values=[task.description, task.user.id, task.duration, task.completed]

#     results=run_sql(sql,values)
#     id=results[0]["id"]
#     task.id=id
#     return task    