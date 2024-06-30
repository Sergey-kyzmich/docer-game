from colorama import Fore as F, Style as S

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



{F.YELLOW}Начать играть - {F.RED}G
{F.YELLOW}Загрузить сохранение - {F.RED}L
{F.YELLOW}Повторно посмотреть описание - {F.RED}S{S.RESET_ALL}
{F.YELLOW}Закрыть игру - {F.RED}ctrl+c{S.RESET_ALL}
"""
        
        self.description_input_name=f"""
В этой игре ты будешь играть за персонажа, по имени:"""


        self.menu2=f"""{F.GREEN}
Выберите действие:

Наведаться на аукцион - {F.RED}a{F.GREEN}
Посмотреть описание - {F.RED}d{S.RESET_ALL}
"""

        self.select_load_name=f"""
Подтвердить - space

Выбрать сохранение под именем: """
        
        self.by_cont_description=f"""{F.GREEN}
Добро пожаловать на аукционе контейнеров!
Тут тебе предстоит побороться за контейнеры.

Контейнеры все различны и разной ценовой категории. 
Ты можешь купить как все, так и ничего.
По истечении 3-х секунд после покупки контейнера контейнер либо покупается, либо ставку перебивают
У контейнеров есть несколько характеристик:

{F.RED}Номер контейнера{F.YELLOW} - Порядковый номер контейнера.
{F.RED}Начальная ставка{F.YELLOW} - Сумма, с которой начинаются торги.
{F.RED}Текущая ставка{F.YELLOW} - Текущая ставка. В случае выигрыша победитель получит контейнер по этой цене.
{F.RED}Следующая ставка{F.YELLOW} - Минимальная ставка, которая может быть установлена в данный момент.(Текущая ставка+10%)
{F.RED}Оценочная стоимость{F.YELLOW} - Примерная стоимость контейнера(Может показать и приблизительно правдивые результаты, так и сильно ошибочные)(В процессе игры ты прокачать уровень оценки стоимости контейнера(изначально-0, максимально-80))
{F.RED}Привезен из{F.YELLOW} - Страна, из которой был привезен контейнер(Влияет на содержимое контейнера)
{F.RED}Тип содержимого{F.YELLOW} - Тип содержимого, которое находится в контейнере(Автомобиль, Одежда/мебель/предметы, Антиквариат, Другое)
{S.RESET_ALL}

{F.GREEN}Так-же не стоит трать все сбережения на контейнеры, ведь никогда не знаешь, доедет ли он до тебя.
Ты можешь оформить страховку на контейнер. Чем больше стоимость контейнера, тем дороже и страховка. В случае трагедии она полностью компенсирует Стоимость контейнера.

{F.GREEN}Вернуться назад - {F.RED}space{F.GREEN}.{S.RESET_ALL}"""
        self.by_cont_1=f"""
{F.GREEN}Сейчас идут торги за 3 контейнера! Выбери более желанный и поставь ставку!{S.RESET_ALL}
"""
        
        self.car_model=[
    "Toyota Camry",
    "Honda Civic",
    "Ford Mustang",
    "Chevrolet Silverado",
    "Nissan Altima",
    "BMW 3 Series",
    "Mercedes-Benz C-Class",
    "Audi A4",
    "Volkswagen Golf",
    "Subaru Outback",
    "Hyundai Elantra",
    "Kia Sorento",
    "Mazda CX-5",
    "Lexus RX",
    "Jeep Wrangler",
    "Range Rover Evoque",
    "Tesla Model 3",
    "Volvo XC90",
    "Porsche 911",
    "Mitsubishi Outlander"
]
        self.clothes= [
    "Rolex Watch",
    "Louis Vuitton Handbag",
    "Hermès Birkin Bag",
    "Gucci Sneakers",
    "Prada Sunglasses",
    "Chanel Perfume",
    "Tom Ford Suit",
    "Burberry Trench Coat",
    "Yves Saint Laurent Wallet",
    "Cartier Bracelet",
    "Balenciaga Hoodie",
    "Versace Dress",
    "Fendi Belt",
    "Givenchy Scarf",
    "Bottega Veneta Clutch",
    "Moncler Down Jacket",
    "Christian Dior Earrings",
    "Alexander McQueen Boots",
    "Ferragamo Shoes",
    "Valentino Garavani Rockstud Bag"
]
        self.anticvar=[
    "Antique Persian Rug",
    "Vintage Gramophone",
    "Victorian Porcelain Doll",
    "Art Deco Lamp",
    "Edwardian Jewelry Box",
    "Georgian Silverware",
    "Ming Dynasty Vase",
    "19th Century Wooden Armoire",
    "Classic Pocket Watch",
    "Renaissance Oil Painting",
    "Hand-carved Cuckoo Clock",
    "Tiffany Stained Glass",
    "French Louis XV Armchair",
    "Art Nouveau Mirror",
    "Antique Globe",
    "Colonial Writing Desk",
    "Jacobean Chest",
    "Old Manuscripts",
    "Japanese Samurai Sword",
    "Hellenistic Statue"
]
        self.other= [
    "Diamond Necklace",
    "Grand Piano",
    "High-end Gaming PC",
    "Luxury Yacht Model",
    "Gold Bullion",
    "Signature Edition Electric Guitar",
    "Premium Leather Sofa",
    "High-end Home Theater System",
    "Designer Watch Collection",
    "Antique Chandelier",
    "Exclusive Artwork",
    "Custom Motorcycle",
    "Professional Camera Equipment",
    "Vintage Wine Collection",
    "Luxury Sports Equipment",
    "Gourmet Kitchen Appliances",
    "Elegant Crystal Glassware",
    "Exotic Car Parts",
    "Smart Home Automation System",
    "Custom-made Furniture"
]
        self.crash_cont = [
    "Контейнер был утерян в море",
    "Контейнер был повреждён во время шторма",
    "Контейнер был перевёрнут во время погрузки на судно",
    "Контейнер был ошибочно отправлен на другой континент",
    "Контейнер был повреждён при аварии грузового автомобиля",
    "Контейнер затопило на складе из-за прорыва трубы",
    "Контейнер пострадал при пожаре в порту",
    "Контейнер был разграблен пиратами",
    "Контейнер был повреждён во время землетрясения",
    "Контейнер был опрокинут в воду сильными ветрами в порту",
    "Контейнер подвергся нападению вандалов",
    "Контейнер уничтожен в порту из-за забастовки рабочих",
    "Контейнер опоздал на судно из-за проблем с документами",
    "Контейнер был случайно разгружен в неправильном порту",
    "Контейнер подвергся актам саботажа",
    "Контейнер повредился при столкновении с другим контейнером",
    "Контейнер подвергся воздействию химических веществ из соседнего контейнера"
]