# pip install pillow - библиотека для работы с картинками
# pip install color-it - позволяет перекрасить текст в любой текст

from PIL import Image  # PIL - билиотека pillow
from colorit import background, init_colorit

# init_colorit() очищает консоль. Background возвращает строку с цветом
init_colorit()
depth = int(input('Размер картинки (1 число): '))

image = Image.open(input('Путь к картинке: '))
image = image.resize((depth, depth))
# так можно получить цвет пикселя по координатам на картинке
# аргументы - координаты Х и У
# в кач-ве аргумента передаётся tupl - кортеж
# print(image.getpixel((100, 200)))

# нужно пройтись по всем пикселям
for y in range(image.size[1]):
    for x in range(image.size[0]):
        # т.е. print() по-дефолту дописывает \n, чтобы был перенос на
        # следующую строку, поэтому 2м аргументом для print
        # указываю end=''. Т.е., затираю символ \n и переноса нет
        print(background(' ', image.getpixel((x, y))), end='')
    print()
