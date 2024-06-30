import keyboard as kb

from text import text as class_text
from extention import extention
import database
import game
text=class_text()



def start():
    database.database().create_db()
    e=extention()
    e.clear_cmd()#Очистка командной строки
    #Старт
    print(text.start)
    kb.wait("space")

    e.clear_cmd()
    print(text.description)

    kb.add_hotkey("g", game.start_new_game)#Создание игры
    kb.add_hotkey("l", game.start_old_game)#Загрузка игры

    kb.wait("s")#Перезапуск описания
    start()
    

if __name__=="__main__":
    start()