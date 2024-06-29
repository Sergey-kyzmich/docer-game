import game_container
import keyboard as kb
from text import text as class_text
from extention import extention
import os
import game

text=class_text()



def start():
    e=extention()
    e.clear_cmd()#Очистка командной строки
    #Старт
    print(text.start)
    kb.wait("space")

    e.clear_cmd()
    print(text.description)

    kb.add_hotkey("b", show_control)# посмотреть управление
    kb.add_hotkey("g", game.new_game)#Создание игры
    kb.add_hotkey("l", game.start_old_game)#Загрузка игры

    kb.wait("s")#Перезапуск описания
    start()
    

    
def show_control():
    print(234)

if __name__=="__main__":
    start()