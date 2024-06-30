import os
import sys
import keyboard as kb
from database import database
from text import text as class_text
import time

class extention:
    def __init__(self):
        self.kb = kb
        self.text=class_text()
        self.k=0

    def clear_cmd(self):
        a = lambda:os.system("cls")
        a()
    
    def show_control():
        print("show_control")

