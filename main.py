print("Это мои первые строчки кода")
print(1 + 2)
print(2 + 4 / 6 * 10)
print(9 // 4)
name = 10
print(name)
i = "Это мои первые строчки кода"
print(i)
n = "10"
m = 20
print(int(n) + m)
print(1)
print("1")
print(n + str(m))
print(f"{n}{m}")
j = f"{m}-''это переменная'"
print(j)
print(n, m)
print(n, f"\n{m}")
name1 = input("Введите число ")
name2 = input("Введите число ")
print(name1 + name2)
name1 = int(input("Введите число "))
name2 = int(input("Введите число "))
print(name1 + name2)
m += 1

# Next

name1 = 10
name2 = 20

if name1 == name2:
    print("name1 > name2")
if name1 >= name2 is True:
    print("True")
    pass
elif name1 < name2:
    print("name1 < name2")
elif name1 != name2:
    pass
else:
    print("name1 = name2")

"""

print("Test message")

"""

for i in 1, 2, 3, "sorry":
    print(i)

for o in "sorry":
    print(o)

# Список [], Кортедж()
n = [1, 2, 3, "sorry"]
for p in n:
    print(p)

m = [1, 2, 3, "sorry"]
print(m[3])

m.append(10)
print(m[4])

o = 0
while o < 10:
    print(o)
    o += 1

# Next
# + Images

import pygame
import random
import os

num = random.randint(0, 100)
print(num)

W = 480
H = 360
SILVER = (192, 192, 192)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Угадай число")
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((W, H))

path = os.path.dirname(os.path.abspath(__file__))
bg = pygame.image.load(os.path.join(path, "Image/room.png"))
bg_rect = bg.get_rect(topleft=(0, 0))
cat = pygame.image.load(os.path.join(path, "Image/cat.png"))
cat_rect = cat.get_rect(topleft=(70, 220))
dog = pygame.image.load(os.path.join(path, "Image/dog.png"))
dog_rect = dog.get_rect(topleft=(410, 220))
owl = pygame.image.load(os.path.join(path, "Image/owl.png"))
owl_rect = owl.get_rect(topleft=(210, 120))
dialog = pygame.image.load(os.path.join(path, "Image/dialog.png"))
dialog_rect = owl.get_rect()
dialog_cat_pos = (cat_rect.x, cat_rect.y - dialog_rect.h)
dialog_dog_pos = (dog_rect.x - dialog_rect.w // 2, dog_rect.y - dialog_rect.h)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False

    screen.blit(bg, bg_rect)
    screen.blit(cat, cat_rect)
    screen.blit(dog, dog_rect)
    screen.blit(owl, owl_rect)
    pygame.display.update()

# Next
# + Images

import pygame
import random
import os

num = random.randint(0, 100)
print(num)

W = 480
H = 360
SILVER = (192, 192, 192)
BLACK = (0, 0, 0)
numeral = ""
movie = 1
block = 0
start = 1
OUTSIDE_BG = (0, -100)

pygame.init()
pygame.display.set_caption("Угадай число")
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((W, H))

font = pygame.font.SysFont("Arial", 28, True, False)
font_box = pygame.Surface((W - 20, font.get_height()))
font_rect = font_box.get_rect(center=(W // 2, H - font.get_height()))
font2 = pygame.font.SysFont("Arial", 14, False, True)

path = os.path.dirname(os.path.abspath(__file__))
bg = pygame.image.load(os.path.join(path, "Image/room.png"))
bg_rect = bg.get_rect(topleft=(0, 0))
cat = pygame.image.load(os.path.join(path, "Image/cat.png"))
cat_rect = cat.get_rect(topleft=(70, 220))
dog = pygame.image.load(os.path.join(path, "Image/dog.png"))
dog_rect = dog.get_rect(topleft=(410, 220))
owl = pygame.image.load(os.path.join(path, "Image/owl.png"))
owl_rect = owl.get_rect(topleft=(210, 120))
dialog = pygame.image.load(os.path.join(path, "Image/dialog.png"))
dialog_rect = owl.get_rect()
dialog_cat_pos = (cat_rect.x, cat_rect.y - dialog_rect.h)
dialog_dog_pos = (dog_rect.x - dialog_rect.w // 2, dog_rect.y - dialog_rect.h)


def dialogs(text, pos, owl_text):
    screen.blit(dialog, pos)
    screen.blit(font2.render(text, True, BLACK), (pos[0] + 5, pos[1] + 5))
    dialog_owl_pos = (owl_rect.x, owl_rect.y - dialog_rect.h)
    screen.blit(dialog, dialog_owl_pos)
    screen.blit(font2.render(owl_text, True, BLACK), (dialog_owl_pos[0] + 5, dialog_owl_pos[1] + 5))
    pygame.display.update()
    pygame.time.wait(2000)


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        # Выход из программы при нажатии на клавишу ESCAPE
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
            # Печатает только цифры
            elif e.unicode.isdecimal() and block == 0:
                numeral += e.unicode

if block == 0:
    screen.blit(bg, bg_rect)
    screen.blit(cat, cat_rect)
    screen.blit(dog, dog_rect)
    screen.blit(owl, owl_rect)
    screen.blit(font_box, font_rect)
    font_box.fill(SILVER)
    font_box.blit(
        font.render(numeral, True, BLACK), (10, 0)
    )
    pygame.display.update()

    if start == 1:
        dialogs("", OUTSIDE_BG, "Я загадал число")
        dialogs("", OUTSIDE_BG, "От 0 до 100")
        dialogs("Кот твой ход", dialog_dog_pos, "Отгадайте его")
        start = 0

# Next
# + Images

import pygame
import random
import os

num = random.randint(0, 100)
print(num)

W = 480
H = 360
SILVER = (192, 192, 192)
BLACK = (0, 0, 0)
numeral = ""
move = 1
block = 0
start = 1
OUTSIDE_BG = (0, -100)

pygame.init()
pygame.display.set_caption("Угадай число")
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((W, H))

font = pygame.font.SysFont("Arial", 28, True, False)
font_box = pygame.Surface((W - 30, font.get_height()))
font_rect = font_box.get_rect(center=(W // 2, H - 30))
font2 = pygame.font.SysFont("Arial", 14, False, True)

path = os.path.dirname(os.path.abspath(__file__))
bg = pygame.image.load(os.path.join(path, "Image/room.png"))
bg_rect = bg.get_rect(topleft=(0, 0))
cat = pygame.image.load(os.path.join(path, "Image/cat.png"))
cat_rect = cat.get_rect(topleft=(70, 220))
dog = pygame.image.load(os.path.join(path, "Image/dog.png"))
dog_rect = dog.get_rect(topleft=(410, 220))
owl = pygame.image.load(os.path.join(path, "Image/owl.png"))
owl_rect = owl.get_rect(topleft=(210, 120))
dialog = pygame.image.load(os.path.join(path, "Image/dialog.png"))
dialog_rect = owl.get_rect()
dialog_cat_pos = (cat_rect.x, cat_rect.y - dialog_rect.h)
dialog_dog_pos = (dog_rect.x - dialog_rect.w // 2, dog_rect.y - dialog_rect.h)
dialog_owl_pos = (owl_rect.x, owl_rect.y - dialog_rect.h)
print(dialog_cat_pos)
print(cat_rect)


def dialogs(text, pos, owl_text):
    screen.blit(dialog, pos)
    screen.blit(font2.render(text, True, BLACK), (pos[0] + 5, pos[1] + 5))
    screen.blit(dialog, dialog_owl_pos)
    screen.blit(font2.render(owl_text, True, BLACK), (dialog_owl_pos[0] + 5, dialog_owl_pos[1] + 5))
    pygame.display.update()
    pygame.time.wait(2000)


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        # Выход из программы при нажатии на клавишу ESCAPE
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
            # Печатает только цифры
            elif e.unicode.isdecimal() and block == 0:
                numeral += e.unicode
            # Удаляет последний элемент
            elif e.key == pygame.K_BACKSPACE:
                numeral = numeral[:-1]
            elif e.key == pygame.K_RETURN and numeral:
                if int(numeral) > 100:
                    dialogs("", OUTSIDE_BG, "Вы ошиблись")
                elif int(numeral) > num:
                    dialogs("", OUTSIDE_BG, "Число меньше")
                elif int(numeral) < num:
                    dialogs("", OUTSIDE_BG, "Число больше")
                if move == 1:
                    if int(numeral) == num:
                        dialogs(f"Это число {numeral}", dialog_cat_pos, "Кот, ты выйграл")
                        block = 1
                    else:
                        dialogs(f"Дог, товой ход", dialog_cat_pos, "Кот, ты выйграл")
                elif move == 2:
                    if int(numeral) == num:
                        dialogs(f"Это число {numeral}", dialog_dog_pos, "Дог, ты выйграл")
                        block = 1
                    else:
                        dialogs(f"Кот, товой ход", dialog_dog_pos, "Продолжаем")
                numeral = ""
                move += 1
                if move > 2:
                    move = 1

if block == 0:
    screen.blit(bg, bg_rect)
    screen.blit(cat, cat_rect)
    screen.blit(dog, dog_rect)
    screen.blit(owl, owl_rect)
    screen.blit(font_box, font_rect)
    font_box.fill(SILVER)
    font_box.blit(
        font.render(numeral, True, BLACK), (10, 0)
    )
    pygame.display.update()

    if start == 1:
        dialogs("", OUTSIDE_BG, "Я загадал число")
        dialogs("", OUTSIDE_BG, "От 0 до 100")
        dialogs("Кот твой ход", dialog_dog_pos, "Отгадайте его")
        start = 0
