from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def catalogue(request):
    bouquets = [
        {"image": "/static/catalogue1.jpg", "name": "Ранункулюсы", "price": "4950 р."},
        {"image": "/static/catalogue2.jpg", "name": "Букет 'Tiara'", "price": "5000 р."},
        {"image": "/static/catalogue3.jpg", "name": "Пионовидные розы", "price": "400 р./1 шт."},
        {"image": "/static/catalogue4.jpg", "name": "Пионы", "price": "500 р./1 шт."},
        {"image": "/static/catalogue5.jpg", "name": "Цветочная сумочка", "price": "7000 р."},
        {"image": "/static/catalogue6.jpg", "name": "Wow Букет", "price": "20000 р."},
        {"image": "/static/catalogue7.jpg", "name": "Тюльпаны", "price": "4000 р."},
        {"image": "/static/catalogue8.jpg", "name": "Букет 'Strawberry Coctail'", "price": "6200 р."},
        {"image": "/static/catalogue9.jpg", "name": "С пионами", "price": "5850 р."},
    ]

    context = {"bouquets": bouquets}
    return render(request, "catalogue.html", context)

def info(request):
    extras = {
        "Открытки": [
            {"name": "Открытка Улыбайся", "image": "/static/info1.jpg"},
            {"name": "Открытка - Рядом", "image": "/static/info2.jpg"},
            {"name": "Открытка - Весна", "image": "/static/info3.jpg"},
        ],
        "Вазы": [
            {"name": "Вазы стеклянные", "image": "/static/info4.jpg"},
            {"name": "Вазы керамические", "image": "/static/info5.jpg"},
            {"name": "Ваза - книга", "image": "/static/info6.jpg"},
        ],
        "Для домашнего ухода": [
            {"name": "Кензан", "image": "/static/info7.jpg"},
            {"name": "Секатор", "image": "/static/info8.jpg"},
            {"name": "Секатор-ножницы", "image": "/static/info9.jpg"},
        ],
    }

    context = {'extras': extras}
    return render(request, 'info.html', context)


def algorithm(request):
    result = None
    books_input = request.GET.get("books", "")

    if books_input:
        books_list = books_input.split(", ")

        books = []
        for book in books_list:
            try:
                name, pages = book.split("-")
                pages = int(pages)
                if pages < 200:
                    books.append((name, pages))
            except ValueError:
                pass

        books.sort(key=lambda x: (-x[1], x[0]))

        result = [book[0] for book in books]

    context = {"result": result}
    return render(request, "algorithm.html", context)



def about(request):
    student = {
        "name": "Хоменко Анастасия Максимовна",
        "photo": "/static/anastasia.jpg",
        "email": "amkhomenko_1@edu.hse.ru",
        "phone": "+79087270757",
    }

    program_description = """
    «Бизнес-информатика» представляет собой междисциплинарное направление, интегрирующее такие дисциплины, как 
    информатика, математика, экономика, менеджмент. По определению IEEE Conference on Business Informatics 
    «Бизнес-информатика представляет собой научное направление, ориентированное на изучение информационных процессов  
    и связанных с ними явлений в социально-экономическом и бизнес контексте…»
    """

    teachers = [
        {
            "name": "Улитин Борис Игоревич",
            "photo": "/static/ulitin.jpg",
            "email": "bulitin@hse.ru",
        },
        {
            "name": "Емельянова Мария Максимовна",
            "photo": "/static/emelyanova.jpg",
            "email": "example@hse.ru",
        }
    ]

    classmates = [
        {
            "name": "Лумбова Софья Игоревна",
            "photo": "/static/sofia.jpg",
            "email": "silumbova@edu.hse.ru",
            "phone": "+79038482926",
        },
        {
            "name": "Щапова Майя Алексеевна",
            "photo": "/static/maya.jpg",
            "email": "maschapova@edu.hse.ru",
            "phone": "+79200516002",
        }
    ]

    context = {
        "student": student,
        "program_description": program_description,
        "teachers": teachers,
        "classmates": classmates
    }

    return render(request, "about.html", context)