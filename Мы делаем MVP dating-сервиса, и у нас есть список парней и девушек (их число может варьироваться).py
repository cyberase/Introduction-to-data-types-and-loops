mens = ['Кайл', 'Эзра', 'Винсент', 'Рами', 'Фил']
womens = ['Гермиона', 'Кира', 'Юки', 'Эмма', 'Эш']
if len(mens) == len(womens):
    print("Идеальная пара:")
    mens.sort()
    womens.sort()
    dating = zip(mens, womens)
    for company in dating:
        print(f"{company[0]} и {company[1]}")
else:

    print("Кто то может остаться без пары")