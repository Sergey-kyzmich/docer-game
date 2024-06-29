import prettytable

#Используется для изменения цвета текста
from colorama import Fore, Back, Style

def show(sum_start=int, sum=int, number=int, location=str, type=str):
    #Создание таблицы(обводка контейнера)
    table = prettytable.PrettyTable()

    next_stavka=f"{Fore.YELLOW}Следующая ставка {sum+sum//10}💲?{Style.RESET_ALL}"
    help_text=f"{Fore.BLUE}Управление(нажмите {Fore.RED}b{Fore.BLUE}){Style.RESET_ALL}"

    number=f"Номер контейнера:{Fore.CYAN} {number}{Style.RESET_ALL}."
    sum_start=f"Начальная ставка:{Fore.YELLOW} {sum_start}{Style.RESET_ALL}💲."
    sum=f"Текущая ставка:{Fore.YELLOW} {sum}{Style.RESET_ALL}💲."
    location=f"Привезен из:{Fore.GREEN} {location}{Style.RESET_ALL}."
    type=f"Тип содержимого:{Fore.GREEN} {type}{Style.RESET_ALL}."


    table.field_names=["name-column"]
    table.add_row([""])
    table.add_row([number])
    table.add_row([sum_start])
    table.add_row([sum])
    table.add_row([location])
    table.add_row([type])
    table.add_row([""])
    table.header=False
    
    #Стили для отображения таблицы
    table.align["name-column"] = "l"
    table.padding_width=10

    table.vrules=prettytable.FRAME
    print(table)
    print()
    print(help_text)
    print()
    print(next_stavka)
    print()
    print(f"{Fore.GREEN}<----  ",  f"  ---->{Style.RESET_ALL}")
show(111,222,1,"russia", "car")