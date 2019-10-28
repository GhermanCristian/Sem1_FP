'''
Module which contains all the regex patterns
COM_ is used for the command-based UI
MEN_ is used for the menu-based UI
'''

UI_TYPE_PATTERN = r'''
    \ *                             # 0 or more spaces
    ([1-2])                         # digits between 1 and 2
    \ *                             # 0 or more spaces
'''

COM_exitPattern = r'''
    \ *                             # 0 or more spaces
    (\b exit \b)                    # "exit" keyword
    \ *                             # 0 or more spaces
'''

COM_addPattern = r'''
    \ *                             # 0 or more spaces
    (\b add \b)                     # "add" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces 
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
'''

COM_insertPattern = r'''
    \ *                             # 0 or more spaces
    (\b insert \b)                  # "insert" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces 
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces
    (\bat\b)                        # "at" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
'''

COM_removePosPattern = r'''
    \ *                             # 0 or more spaces
    (\b remove \b)                  # "remove" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
'''

COM_removeRangePattern = r'''
    \ *                             # 0 or more spaces
    (\b remove \b)                  # "remove" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces
    (\b to \b)                      # "to" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
'''

COM_removePropertyPattern = r'''
    \ *                             # 0 or more spaces
    (\b remove \b)                  # "remove" keyword
    \ +                             # 1 or more spaces
    ( < | = | > )                   # comparator
    \ +                             # 1 or more spaces
    (\d* \.? \d*)                   # floating point value
    \ *                             # 0 or more spaces
'''

COM_replacePattern = r'''
    \ *                             # 0 or more spaces
    (\b replace \b)                 # "replace" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces
    (\b with \b)                    # "with" keyword
    \ +                             # 1 or more spaces
    (\b P1 \b | \b P2 \b | \b P3 \b)# P1, P2 or P3
    \ *                             # 0 or more spaces
'''

COM_listPattern = r'''
    \ *                             # 0 or more spaces
    (\b list \b)                    # "list" keyword
    \ *                             # 0 or more spaces
'''

COM_listSortedPattern = r'''
    \ *                             # 0 or more spaces
    (\b list \b)                    # "list" keyword
    \ +                             # 1 or more spaces
    (\b sorted \b)                  # "sorted" keyword
    \ *                             # 0 or more spaces
'''

COM_listPropertyPattern = r'''
    \ *                             # 0 or more spaces
    (\b list \b)                    # "list" keyword
    \ +                             # 1 or more spaces
    ( < | = | > )                   # comparator
    \ +                             # 1 or more spaces
    (\d* \.? \d*)                   # floating point value
    \ *                             # 0 or more spaces
'''

COM_averagePattern = r'''
    \ *                             # 0 or more spaces
    (\b avg \b)                     # "avg" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces
    (\b to \b)                      # "to" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
'''

COM_minimumPattern = r'''
    \ *                             # 0 or more spaces
    (\b min \b)                     # "min" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces
    (\b to \b)                      # "to" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
'''

COM_topAveragePattern = r'''
    \ *                             # 0 or more spaces
    (\b top \b)                     # "top" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
'''

COM_topProblemPattern = r'''
    \ *                             # 0 or more spaces
    (\b top \b)                     # "top" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
    (\b P1 \b | \b P2 \b | \b P3 \b)# P1, P2 or P3
    \ *                             # 0 or more spaces
'''

COM_undoPattern = r'''
    \ *                             # 0 or more spaces
    (\b undo \b)                    # "undo" keyword
    \ *                             # 0 or more spaces
'''

MEN_exitPattern = r'''
    \ *                             # 0 or more spaces
    (\b 0 \b)                       # "exit" keyword
    \ *                             # 0 or more spaces
'''

MEN_addPattern = r'''
    \ *                             # 0 or more spaces
    (\b 1 \b)                       # "add" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces 
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
'''

MEN_insertPattern = r'''
    \ *                             # 0 or more spaces
    (\b 2 \b)                       # "insert" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces 
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces
    (\bat\b)                        # "at" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
'''

MEN_removePosPattern = r'''
    \ *                             # 0 or more spaces
    (\b 3 \b)                       # "remove" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
'''

MEN_removeRangePattern = r'''
    \ *                             # 0 or more spaces
    (\b 3 \b)                       # "remove" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces
    (\b to \b)                      # "to" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
'''

MEN_removePropertyPattern = r'''
    \ *                             # 0 or more spaces
    (\b 3 \b)                       # "remove" keyword
    \ +                             # 1 or more spaces
    ( < | = | > )                   # comparator
    \ +                             # 1 or more spaces
    (\d* \.? \d*)                   # floating point value
    \ *                             # 0 or more spaces
'''

MEN_replacePattern = r'''
    \ *                             # 0 or more spaces
    (\b 4 \b)                       # "replace" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces
    (\b with \b)                    # "with" keyword
    \ +                             # 1 or more spaces
    (\b P1 \b | \b P2 \b | \b P3 \b)# P1, P2 or P3
    \ *                             # 0 or more spaces
'''

MEN_listPattern = r'''
    \ *                             # 0 or more spaces
    (\b 5 \b)                       # "list" keyword
    \ *                             # 0 or more spaces
'''

MEN_listSortedPattern = r'''
    \ *                             # 0 or more spaces
    (\b 5 \b)                       # "list" keyword
    \ +                             # 1 or more spaces
    (\b sorted \b)                  # "sorted" keyword
    \ *                             # 0 or more spaces
'''

MEN_listPropertyPattern = r'''
    \ *                             # 0 or more spaces
    (\b 5 \b)                       # "list" keyword
    \ +                             # 1 or more spaces
    ( < | = | > )                   # comparator
    \ +                             # 1 or more spaces
    (\d* \.? \d*)                   # floating point value
    \ *                             # 0 or more spaces
'''

MEN_averagePattern = r'''
    \ *                             # 0 or more spaces
    (\b 6 \b)                       # "avg" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces
    (\b to \b)                      # "to" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
'''

MEN_minimumPattern = r'''
    \ *                             # 0 or more spaces
    (\b 7 \b)                       # "min" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ +                             # 1 or more spaces
    (\b to \b)                      # "to" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
'''

MEN_topAveragePattern = r'''
    \ *                             # 0 or more spaces
    (\b 8 \b)                       # "top" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
'''

MEN_topProblemPattern = r'''
    \ *                             # 0 or more spaces
    (\b 8 \b)                       # "top" keyword
    \ +                             # 1 or more spaces
    (\d+)                           # 1 or more digits
    \ *                             # 0 or more spaces
    (\b P1 \b | \b P2 \b | \b P3 \b)# P1, P2 or P3
    \ *                             # 0 or more spaces
'''

MEN_undoPattern = r'''
    \ *                             # 0 or more spaces
    (\b 9 \b)                       # "undo" keyword
    \ *                             # 0 or more spaces
'''

COM_patternList = [
    COM_exitPattern, 
    COM_addPattern, 
    COM_insertPattern,
    COM_removePosPattern, 
    COM_removeRangePattern, 
    COM_removePropertyPattern, 
    COM_replacePattern, 
    COM_listPattern,
    COM_listSortedPattern,
    COM_listPropertyPattern, 
    COM_averagePattern, 
    COM_minimumPattern, 
    COM_topAveragePattern,
    COM_topProblemPattern,
    COM_undoPattern
]

MEN_patternList = [
    MEN_exitPattern, 
    MEN_addPattern, 
    MEN_insertPattern,
    MEN_removePosPattern, 
    MEN_removeRangePattern, 
    MEN_removePropertyPattern, 
    MEN_replacePattern, 
    MEN_listPattern,
    MEN_listSortedPattern,
    MEN_listPropertyPattern, 
    MEN_averagePattern, 
    MEN_minimumPattern, 
    MEN_topAveragePattern,
    MEN_topProblemPattern,
    MEN_undoPattern    
]