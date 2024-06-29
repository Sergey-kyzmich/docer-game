from text import text
from database import database
from extention import extention
import keyboard as kb
class new_game:
    def __init__(self):
        print("init")



def start_new_game():
    cl = new_game()
    # Получение имени пользователя
    name_user=input(text.description_input_name)



def start_old_game():
    e = extention()
    select_name=True
    k=0
    name = e.select_name(-1)
    print(f"{name=}")
            