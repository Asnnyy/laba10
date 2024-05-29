import json
def z1():
    with open('text.json', 'r', encoding='utf8') as f:
        c = json.load(f)
        p = c['products']
        for product in p:
            if product['available']:
                available = "In stock"
            else:
                available = "Product out of stock"
            print("Название:", product['name'], '\n', "Цена:", product['price'], '\n', "Вес:", product['weight'], '\n', available)
z1()
def z3():
    new = {}
    with open('en-ru.txt', 'r', encoding='utf-8') as f:
        for i in f:
            en, ru = i.strip().split('-')
            for s in ru.split(','):
                if s not in new:
                    new[s] = [en]
                else:
                    new[s].append(en)
    a = dict(sorted(new.items()))
    with open('new.txt', 'w', encoding='utf-8') as f:
        for key, value in a.items():
            f.write(f'{key} - {value} \n')
z3()




