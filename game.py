from text import text
from database import database
from extention import extention
import keyboard as kb
import time
class new_game:
    def __init__(self):
        print("init")
        self.name_user=""
        self.e=extention()
        self.text=text()
        self.db = database()
        self.renta=0

    def start(self):
        self.e.clear_cmd()
        user = self.db.get_line(self.name_user)
        self.money=user[1]
        self.level=user[2]
        self.item=user[3]
        print("Добро пожаловать в главном меню!")
        print(f"Деньги: {self.money}")
        print(f"Дневная рента: {self.renta}")
        print(self.text.menu2)

        kb.add_hotkey("a", self.by_cont)
        kb.add_hotkey("c", self.go_check_conts)
    
    def by_cont(self):
        self.e.clear_cmd()
        print("go to cont")
        
    
    def go_check_conts(self):
        self.e.clear_cmd()
        print("go to check conts")



def start_new_game():
    ng = new_game()
    # Получение имени пользователя
    name_user=""
    while name_user=="":input(text.description_input_name)

    ng.start()



def start_old_game():
    e = extention()
    k=0
    kb.unhook_all_hotkeys()
    db = database()
    # for item in db.get_all():
    #     name_list.append(item[0])
    name_list=["name1", "name2", "name3", "name4"]
    
    def show_select_name():
        e.clear_cmd()
        print("Выберите персонажа:")
        for i in name_list:
            print(i)
    show_select_name()
    name=""

    while name not in name_list:
        show_select_name()
        name = input("Имя: ")

    e.clear_cmd()
    print("suc")
    ng = new_game()
    ng.start()
            