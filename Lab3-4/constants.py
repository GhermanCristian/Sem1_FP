UI_PROMPT_TEXT = '''
    1. Command-based UI
    2. Menu-based UI
    
'''

MENU_UI_TEXT = '''
    0. Exit
        - no arguments
    1. Add
        - 3 integers between 0 and 10
    2. Insert
        - 3 integers between 0 and 10
        - "at"
        - 1 integer
    3. Remove
        * removePosition:
            - 1 integer
        * removeRange:
            - 1 integer
            - "to"
            - 1 integer
        * removeWithProperty
            - 1 comparator (<, =, >)
            - 1 float between 0 and 10
    4. Replace
        - 1 integer
        - P1, P2, P3
        - "with"
        - 1 integer between 0 and 10
    5. List
        * default:
            - no arguments
        * sorted
            - "sorted"
        * with property
            - 1 comparator (<, =, >)
            - 1 float between 0 and 10
    6. Average
        - 1 integer
        - "to"
        - 1 integer
    7. Minimum
        - 1 integer
        - "to"
        - 1 integer
    8. Top
        * top by average grade:
            - 1 integer
        * top by average score of a problem
            - 1 integer
            - P1, P2, P3
    9. Undo
        - no arguments

'''