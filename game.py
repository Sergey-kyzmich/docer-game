import keyboard as kb
import time
import random
import prettytable

from text import text
from database import database
from extention import extention
from colorama import Fore, Style #Используется для изменения цвета текста
class new_game:
    def __init__(self, name_user):
        self.go_all_time=False
        self.name_user=name_user
        self.by_select_cont=0
        self.my_cont=[False, False, False]
        self.db = database()
        self.user = self.db.get_line(self.name_user)
        self.money=self.user[1]
        self.level=self.user[2]
        self.e=extention()
        self.opov=''
        self.text=text()

    def start(self):
        self.e.clear_cmd()
        self.check_on_go_game()
        print("Добро пожаловать в главном меню!")
        print(f"Деньги: {int(self.money)}")
        print(f"Уровень оценки стоимости: {self.level}")
        print(self.text.menu2)

        
        kb.unhook_all_hotkeys()
        kb.add_hotkey("a", self.by_cont)
        kb.add_hotkey("d", self.description)
    
    def check_on_go_game(self):
        def callback_y():
            self.go_all_time=True
            self.start()
        def callback_n():exit()
        if not (self.go_all_time):
            if self.money>=1000000:
                print(f"{Fore.GREEN}Вы победили!{Style.RESET_ALL}")
                print(f"Желаете ли вы продолжть играть до бесконечности? \nда - y \nнет - n")
                kb.add_hotkey("y", callback_y)
                kb.add_hotkey("n", callback_n)
            elif self.money<1000:
                self.e.clear_cmd()
                print(f"{Fore.RED}Вы проиграли!{Style.RESET_ALL}")
                exit()
    def description(self):
        self.e.clear_cmd()
        print(self.text.by_cont_description)
        kb.unhook_all_hotkeys()
        kb.add_hotkey("space", self.start)


    def add_min_bid(self):
        if self.my_cont[self.by_select_cont]==False:
            if self.money>=self.by_cont_list[self.by_select_cont]["sum"]*1.1:
                self.by_cont_list[self.by_select_cont]["sum"]=self.by_cont_list[self.by_select_cont]["sum"]*1.1
                self.my_cont[self.by_select_cont]=True
                self.money-=self.by_cont_list[self.by_select_cont]["sum"]*1.1
                self.db.edit(data={
                        "name":self.name_user,
                        "money":self.money,
                        "level":self.level
                    })
                self.show_cont()
                self.interrupt()

    def add_my_bid(self):
        self.e.clear_cmd()
        while True:
            for _ in range(40):kb.send("backspace")
            sum = input("Введите сумму(0-отмена):")
            # try:
            if sum=="0":
                return self.show_cont()
            elif int(sum)<self.by_cont_list[self.by_select_cont]["sum"]+self.by_cont_list[self.by_select_cont]["sum"]//10:
                self.e.clear_cmd()
                print("Сумма должна быть больше либо равна текущей ставке+10%")
            else:
                if self.my_cont[self.by_select_cont]==False:
                        if self.money>=sum:
                            if sum>=self.by_cont_list[self.by_select_cont]["sum"]*1.1:
                                self.by_cont_list[self.by_select_cont]["sum"] = int(sum)
                                self.my_cont[self.by_select_cont]=True
                                self.money-=sum
                                self.db.edit(data={
                            "name":self.name_user,
                            "money":self.money,
                            "level":self.level
                        })
                                return self.interrupt()
                            else:
                                self.show_cont()
                        else:
                            self.show_cont()
                
        
    def scrol_cont_left(self):
        if self.by_select_cont!=0:
            self.by_select_cont-=1
            self.show_cont()
    
    def scrol_cont_right(self):
        if self.by_select_cont!=2:
            self.by_select_cont+=1
            self.show_cont()


    def interrupt(self):
        rand = random.randint(0, 3)
        if rand!=0:
            self.by_cont_list[self.by_select_cont]["sum"]=self.by_cont_list[self.by_select_cont]["sum"]+self.by_cont_list[self.by_select_cont]["sum"]//10
            self.my_cont[self.by_select_cont]=False
            self.show_cont()
            self.opov='no'
            self.money+=self.by_cont_list[self.by_select_cont]["sum"]
        else:
            self.opov='yes'
            self.show_cont()
            

    def by_cont(self):
        self.e.clear_cmd()
        self.by_cont_list=self.create_cont()
        
        kb.unhook_all_hotkeys()
        kb.add_hotkey("b", self.add_min_bid)
        kb.add_hotkey("shift+b", self.add_my_bid)
        kb.add_hotkey("left", self.scrol_cont_left)
        kb.add_hotkey("right", self.scrol_cont_right)
        kb.add_hotkey("space", self.start)
        kb.add_hotkey("p", self.end_by)
        self.time_by_cont = 20
        self.k=0
        self.show_cont()
        

    def end_by(self):
        self.e.clear_cmd()
        if random.randint(0, 10)!=0:#True-катастрофа произошла
            if sum(self.my_cont)>0:
                print(f"Ты выкупил контейнеры под номерами:", end="")
                for i in range(len(self.my_cont)):
                    print(f" {i}" if self.my_cont[i]==True else "")
                win_sum=sum([s['real_sum'] for s in self.by_cont_list if self.my_cont[self.by_cont_list.index(s)]])
                
                self.money+=win_sum
                self.level+=1
                self.db.edit(data={
                    "name":self.name_user,
                    "money":self.money,
                    "level":self.level
                })
                print(f"""
Общей стоимостью: {win_sum}""")
                print()
                print("В контейнере ты нашел: ", end="")
                if self.by_cont_list[self.by_select_cont]["type"]=="Автомобиль":
                    print(self.text.car_model[random.randint(0, len(self.text.car_model)-1)])
                elif self.by_cont_list[self.by_select_cont]["type"]=="Одежда/мебель/предметы":
                    print(self.text.clothes[random.randint(0, len(self.text.clothes)-1)])
                elif self.by_cont_list[self.by_select_cont]["type"]=="Антиквариат":
                    print(self.text.anticvar[random.randint(0, len(self.text.anticvar)-1)])
                else:
                    print(self.text.other[random.randint(0, len(self.text.other)-1)])
            else:print("Ничего, повезет в следующий раз")
        
        else:
            print(f"{Fore.YELLOW}Произошла катастрофа!")
            print(Fore.RED, self.text.crash_cont[random.randint(0, len(self.text.crash_cont)-1)])
            print(f"{Fore.YELLOW}Содержимое контейнера уничтожено{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Выйти - {Fore.RED}space{Style.RESET_ALL}")



        
    
    def create_cont(self):
        level = self.level
        conts = []
        array_sum_start=[[1, 5], [10, 100], [100, 1000]]
        location_array=["Россия", "США", "Япония", "Китай", "Канада", "Германия", "Великобритания", "Неизвестно"]
        type_array=["Автомобиль", "Одежда/мебель/предметы", "Антиквариат", "Другое"]
        for i in range(3):
            data = {}
            data["sum_start"]=random.randint(array_sum_start[i][0], array_sum_start[i][1])*1000
            data["sum"]=data["sum_start"]
            data["number"]=i+1
            data["location"]=location_array[random.randint(0, len(location_array)-1)]
            data["type"]=type_array[random.randint(0, len(type_array)-1)]
            # С шансом в 20% может попасться контейнер, который стоит кратно больше обычных
            real_sum_array=[random.randint(data["sum_start"]//3, int(data["sum_start"]*1.67)), random.randint(data["sum_start"]//2, int(data["sum_start"]*5))]
            data["real_sum"] = real_sum_array[0 if random.randint(0, 5)==0 else 1]
            #алгоритм подсчета оценочной стоимости с учетом уровня игрока
            data["assessed_sum"]=min(data["sum_start"]*5,random.randint(int(data["real_sum"]-min(data["real_sum"]*(1-level/100), data["real_sum"]*0.8)), int(data["real_sum"]+data["real_sum"]*(2-1*(level/100)))))

            conts.append(data)
        return conts



    def show_cont(self):
        self.check_on_go_game()
        sum_start=self.by_cont_list[self.by_select_cont]["sum_start"], 
        sum=self.by_cont_list[self.by_select_cont]["sum"], 
        number=self.by_cont_list[self.by_select_cont]["number"], 
        location=self.by_cont_list[self.by_select_cont]["location"], 
        type=self.by_cont_list[self.by_select_cont]["type"], 
        assessed_sum=self.by_cont_list[self.by_select_cont]["assessed_sum"]
        table = prettytable.PrettyTable()

        next_stavka = sum[0]+sum[0]//10
        next_stavka=f"{Fore.YELLOW}Следующая ставка {int(next_stavka)}💲?{Style.RESET_ALL}"
        help_text=f"""
{Style.RESET_ALL}Поставить минимальную ставку - {Fore.RED}B
{Fore.YELLOW}Поставить свою ставку - {Fore.RED}shift+B
{Fore.YELLOW}Листать список контейнеров - {Fore.RED}Стрелка вправо/влево
{Fore.YELLOW}Уйти с аукциона - {Fore.RED}space
"""

        number=f"Номер контейнера:{Fore.CYAN} {number[0]}{Style.RESET_ALL}."
        sum_start=f"Начальная ставка:{Fore.YELLOW} {sum_start[0]}{Style.RESET_ALL}💲."
        sum=f"Текущая ставка:{Fore.YELLOW} {int(sum[0])}{Style.RESET_ALL}💲."
        assessed_sum=f"Оценочная стоимость:{Fore.YELLOW}{assessed_sum}{Style.RESET_ALL}"
        location=f"Привезен из:{Fore.GREEN} {location[0]}{Style.RESET_ALL}."
        type=f"Тип содержимого:{Fore.GREEN} {type[0]}{Style.RESET_ALL}."


        table.field_names=["name-column"]
        table.add_row([""])
        table.add_row([number])
        table.add_row([sum_start])
        table.add_row([sum])
        table.add_row([assessed_sum])
        table.add_row([location])
        table.add_row([type])
        table.add_row([""])
        table.header=False

        #Стили для отображения таблицы
        table.align["name-column"] = "l"
        table.padding_width=10

        self.e.clear_cmd()
        print(self.text.by_cont_1)
        print(table)
        print(help_text)
        print(next_stavka, end="\n\n")
        print(f"""Деньги на счету: {int(self.money)}
Уровень оценки содержимого: {self.level}""", end="\n\n")
        strelka_array=[f"{Fore.GREEN}---->{Style.RESET_ALL}",
                       f"{Fore.GREEN}<----    ---->{Style.RESET_ALL}",
                       f"{Fore.GREEN}<----{Style.RESET_ALL}"]
        print(strelka_array[self.by_select_cont])
        if self.opov=="yes":print(f"{Fore.YELLOW}Оповещение: {Fore.GREEN}Ваша ставка финальная{Style.RESET_ALL}")
    
        elif self.opov=="no":print(f"{Fore.YELLOW}Оповещение: {Fore.RED}Вашу ставку перебили!{Style.RESET_ALL}")
        

def start_new_game():
    # Получение имени пользователя
    name_user=""
    extention().clear_cmd()
    name_list=[]
    db = database()
    for item in db.get_all():
        name_list.append(item[0])
    kb.send("backspace")
    kb.send("backspace")
    while name_user=="" and name_user not in name_list:
        name_user=input(text().description_input_name)
        extention().clear_cmd()
    
    user={"name":name_user, 
          "money":5000, 
          "level":0}
    db.add_user(user=user)
    ng = new_game(name_user=name_user)
    ng.start()



def start_old_game():
    e = extention()
    kb.unhook_all_hotkeys()
    db = database()
    name_list=[]
    for item in db.get_all():
        name_list.append(item[0])
    # name_list=["name1", "name2", "name3", "name4"]
    name=""
    def show_select_name():
        e.clear_cmd()
        print("Выберите персонажа:")
        for i in name_list:
            print(i)
    show_select_name()
    name=""
    #Требуется, чтобы удалить лишние символы из ввода    
    for _ in range(10):kb.send("backspace")
    while name not in name_list:
        show_select_name()

        name = input("Имя: ")

    e.clear_cmd()
    ng = new_game(name_user=name)
    ng.start()
            