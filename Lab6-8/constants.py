MENU_TEXT = """
    Command list:
    0. Exit
    1. Add new client
        - name
    2. Remove client
        - ID
    3. Update client
        - ID
        - "name" newName
    4. Add new movie
        - title description genre
    5. Remove movie
        - ID
    6. Update movie
        - ID
        - "title" newTitle
        - "description" newDescription
        - "genre" newGenre 
    7. Print list
        - "client"
        - "movie"
    8. Rent a movie
        - clientID movieID rentDate dueDate
    9. Return a movie
        - clientID movieID
    10. Search for clients
        - ID or name
    11. Search for movies
        - ID, title, description or genre
    12. Most active:
        - "client" or "movie"
    13. Late rentals
    14. Undo
    15. Redo
"""

COMMAND_COUNT = 15

MOVIE_FILE = "Data\\Movies.txt"
CLIENT_FILE = "Data\\Clients.txt"

CLIENT_COUNT = 10
MOVIE_COUNT = 10

