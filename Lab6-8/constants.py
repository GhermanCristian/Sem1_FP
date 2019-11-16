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
        - clientID movieID dueDate
    9. Return a movie
        - clientID movieID
    10. *search
    11. *statistics
    12. undo / redo
"""

COMMAND_COUNT = 14

MOVIE_FILE = "Data//Movies.txt"
CLIENT_FILE = "Data//Clients.txt"