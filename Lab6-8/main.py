'''
    Assignment 6-8-9; due on 19/26 Nov 2019, 03/10 Dec 2019
    Problem 3 - movie rental
'''

from UI.normalUI import UI
from UI.GUI import GUI
from settings import Settings

def main():
    if Settings().UI == "normalUI":
        mainProgram = UI()
    else:
        mainProgram = GUI()
    
    mainProgram.start()

if __name__ == "__main__":
    main()