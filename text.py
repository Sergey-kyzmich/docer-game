from colorama import Fore as F, Back as B, Style as S

class text():
    def __init__(self):
        self.start=f"""
{F.GREEN}Добро пожаловать в {F.RED}ЛЕГЕНДАРНУЮ БИТВУ КОНТЕЙНЕРОВ{F.GREEN}!

В этой игре тебе потребуется торговаться, открывать контейнеры с неизвестным содержимим, которое затем потребуется продать.

Управление выполняется с помощью клавиатуры. Нажми {F.RED}ПРОБЕЛ{F.GREEN}.{S.RESET_ALL}"""
        #
        self.description=f"""{F.GREEN}
Каждый контейнер может скрывать ценные предметы или бесполезный хлам. 
Тебе потребуется использовать свой опыт(даже если он равен 0), интуицию и знания, 
чтобы оценить стоимость контейнеров и выиграть самые прибыльные лоты.


{F.YELLOW}Посмотреть управление - {F.RED}B
{F.YELLOW}Начать играть - {F.RED}G
{F.YELLOW}Загрузить сохранение - {F.RED}L
{F.YELLOW}повторно посмотреть описание - {F.RED}S{S.RESET_ALL}
"""
        
        self.description_input_name=f"""
В этой игре ты будешь играть за персонажа, по имени:"""

        self.menu=f""""""

        self.select_load_name=f"""
Подтвердить - space

Выбрать сохранение под именем:"""
        
    

    