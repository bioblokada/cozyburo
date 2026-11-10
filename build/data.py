# -*- coding: utf-8 -*-
# Исходные данные сайта. Фото: папка в /home/claude/photos, номера файлов (префикс NN_).
SRC = '/home/claude/photos'

PROJECTS = [
    dict(slug='teburasi', name='Тебураси', logo='teburasi', kind='Изакая', year='2020',
         address='Страстной бульвар, 7, стр. 3', folder='Тебураси',
         cover=2, photos=[2, 5, 18, 19, 13, 1, 4, 16, 12, 22, 8, 0, 15, 6], section='commercial'),
    dict(slug='riesling-boyz', name='Riesling Boyz', logo='riesling-boyz', kind='Винный бар', year='2020',
         address='Сретенка, 16/2', folder='РИСЛИНГ',
         cover=0, photos=[0, 1, 2, 5, 6, 9, 11, 14, 7, 8, 13, 15, 3, 17], section='commercial'),
    dict(slug='shashlychnaya-mayakovskaya', name='Горбуфет Шашлычная', logo='shashlychnaya', sub='Маяковская', kind='Шашлычная', year='2024',
         address='2-я Тверская-Ямская, 2', folder='Маяковская',
         cover=2, photos=[2, 1, 15, 16, 3, 14, 7, 8, 9, 6, 11, 12, 13, 4], section='commercial'),
    dict(slug='shashlychnaya-pyatnitskaya', name='Горбуфет Шашлычная', logo='shashlychnaya', sub='Пятницкая', kind='Шашлычная', year='2023',
         address='Пятницкая, 16, стр. 1', folder='Пятницкая',
         cover=13, photos=[13, 9, 14, 0, 2, 6, 19, 16, 1, 3, 11, 12, 5, 10], section='commercial'),
    dict(slug='rusalochka-sushi', name='Русалочка Суши', logo='rusalochka-sushi', kind='Суши-бар', year='2021',
         address='Страстной бульвар, 7, стр. 3', folder='Русалочка Страстной',
         cover=16, photos=[16, 9, 12, 3, 1, 2, 6, 7, 8, 4, 14, 19, 10], section='commercial'),
    dict(slug='shashlychnaya-kutuzovskaya', name='Горбуфет Шашлычная', logo='shashlychnaya', sub='Кутузовская', kind='Шашлычная', year='2025',
         address='Кутузовский проспект, 36А', folder='Кутуза',
         cover=14, photos=[14, 17, 19, 10, 16, 2, 9, 13, 1, 6, 12, 4, 18], section='commercial'),
    dict(slug='rusalochka-asia', name='Русалочка Азия', logo='rusalochka-asia', kind='Азиатский ресторан', year='2025',
         address='Ходынский бульвар, 20А', folder='Русалка',
         cover=5, photos=[5, 0, 2, 13, 17, 15, 3, 7, 9, 12, 18, 19, 14, 11], section='commercial'),
    dict(slug='pelmennaya', name='Горбуфет Пельменная', logo='pelmennaya', kind='Пельменная', year='2022',
         address='Малая Дмитровка, 3', folder='Пельменная',
         cover=16, photos=[16, 10, 3, 15, 1, 2, 4, 7, 8, 9, 13, 5, 0], section='commercial'),
    dict(slug='shashlychnaya-paveletskaya', name='Горбуфет Шашлычная', logo='shashlychnaya', sub='Павелецкая', kind='Шашлычная', year='2025',
         address='Новокузнецкая, 39', folder='Павелецкая',
         cover=6, photos=[6, 2, 7, 0, 5, 8, 11, 1, 3, 4, 9, 12, 10], section='commercial', warm=True),
    dict(slug='apartment', name='Квартира', kind='Жилой интерьер', year='',
         address='Москва', folder='квартира',
         cover=37, photos=[37, 38, 31, 22, 42, 2, 5, 14, 19, 24, 27, 43, 17, 33], section='private', teaser='Эксклюзив журнала «Интерьер+Дизайн»'),
]

# Объекты без фото — только строкой
MORE_COMMERCIAL = []

PORTRAIT = SRC + '/корень/00_DSC_6707.jpg'
