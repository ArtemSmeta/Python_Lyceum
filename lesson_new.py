import random

name = "Name"
hp = random.randint(70, 100)
money = random.randint(700, 1010)
luck = random.randint(1, 10)
is_blessed = True
is_immortal = False

print('Вы посмотрели в волшебное зеркало, на нем появляется мутная надпись - привет, {}'.format(name.upper()))


''' 
### Таверна ### 
Зайдя в нее, нужно перебрать список людей в ней и выделить тех, кому больше 18 лет для продолжения общения. Вывести имена этих людей
'''
def find_friend(db, age):
    pass



def aura_color(is_blessed, is_immortal, hp):
    aura_visible = is_blessed & (hp > 50) | is_immortal
    if aura_visible:
        color = "green"
    else:
        color = "red"
    return color


def health_status(hp, is_blessed):
    if hp == 100:
        status = 'is in excellent condition!'
    elif hp in range(90, 100):
        status = "has a few scratches."
    elif hp in range(75, 90):
        if is_blessed:
            status = "has some minor wounds, but is healing quite quickly!"
        else:
            status = "has some minor wounds."
    elif hp in range(15, 75):
        status = "looks pretty hurt."
    else:
        status = "is in awful condition!"
    return status
    
def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
        
        
print(convert_base('1000101011', from_base=2))

print(int('1000101011', 2))
