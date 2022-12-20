from random import randint


def attack(char_name: str, char_class: str) -> str:
    """Define character's attack."""
    if char_class == 'warrior':
        warrior_damage: int = 5 + randint(3, 5)
        return (f'{char_name} нанёс урон противнику равный {warrior_damage}')
    if char_class == 'mage':
        mage_damage: int = 5 + randint(5, 10)
        return (f'{char_name} нанёс урон противнику равный {mage_damage}')
    if char_class == 'healer':
        healer_damage: int = 5 + randint(-3, -1)
        return (f'{char_name} нанёс урон противнику равный {healer_damage}')
    return (f'{char_name} не атаковал!')


def defence(char_name: str, char_class: str) -> str:
    """Define character's defence."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return (f'{char_name} не защищался!')


def special(char_name: str, char_class: str) -> str:
    """Define character's special ability."""
    if char_class == 'warrior':
        w_special: str = f'«Выносливость {80 + 25}»'
        return (f'{char_name} применил специальное умение {w_special}')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита {10 + 30}»')
    return (f'{char_name} не применил специальное умение!')


def start_training(char_name: str, char_class: str) -> str:
    """Start training and give an option to choose an action."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print(
        'Введи одну из команд: attack — чтобы атаковать противника,'
        'defence — чтобы блокировать атаку противника'
        'или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    """Choose class and see the definition of it."""
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input(
            'Введи название персонажа, за которого хочешь играть:'
            'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print(
                'Воитель — дерзкий воин ближнего боя.'
                'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print(
                'Маг — находчивый воин дальнего боя.'
                'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print(
                'Лекарь — могущественный заклинатель.'
                'Черпает силы из природы, веры и духов.')
        approve_line = (
            'Нажми (Y), чтобы подтвердить выбор,'
            'или любую другую кнопку, чтобы выбрать другого персонажа '
        )
        approve_choice = input(approve_line).lower()
    return char_class
