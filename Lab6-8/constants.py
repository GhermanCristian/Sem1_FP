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

MOVIE_FILE = "C:\\Users\\gherm\\Documents\\EclipseWorkspace\\FP\\Labs\\Lab6-8\\Data\\Movies.txt"
CLIENT_FILE = "C:\\Users\\gherm\\Documents\\EclipseWorkspace\\FP\\Labs\\Lab6-8\\Data\\Clients.txt"

CLIENT_COUNT = 10
MOVIE_COUNT = 10
RENTAL_COUNT = 15

#################
# GUI CONSTANTS #
#################

FPS = 30
WINDOW_WIDTH = 1536
WINDOW_HEIGHT = 864
LATERAL_MARGIN = 15
UPPER_MARGIN = 15
LOWER_MARGIN = 10

#command and pageChange boxes
GAP_SIZE = 7
BOX_WIDTH = 150
BOX_HEIGHT = 136

#the input and error bar
BAR_HEIGHT = 50
BAR_WIDTH = WINDOW_WIDTH - 2 * LATERAL_MARGIN

#the panel which will print all the info
PANEL_HEIGHT = 4 * BOX_HEIGHT + 3 * GAP_SIZE
PANEL_WIDTH = 1000

BG_COLOR = (60,  60, 100)
BOX_COLOR = (0, 128, 0)
BAR_COLOR = (100, 100, 100)
TEXT_COLOR = (255, 255, 255)

GAME_FONT = "arial"
GAME_FONT_SIZE = 18

APP_TITLE = "Assignment 6-8"

ITEMS_PER_PAGE = 6

#print (WINDOW_HEIGHT - (3 * UPPER_MARGIN + LOWER_MARGIN + 2 * BAR_HEIGHT + 4 * GAP_SIZE + 5 * BOX_HEIGHT))
#print (WINDOW_WIDTH - (4 * LATERAL_MARGIN + 2 * GAP_SIZE + 3 * BOX_WIDTH + PANEL_WIDTH))
