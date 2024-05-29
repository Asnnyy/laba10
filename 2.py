import json
def z2():
    with open("t1.json", "r", encoding="utf8") as f:
        c = json.load(f)
        name = input("Название продукта:")
        price = int(input("Цена продукта:"))
        weight = int(input("Вес продукта:"))
        available = input("Доступен продукт?:").lower() == "да"
        product = {'Название': name, 'Цена': price, 'Наличие': available, 'Вес': weight}
        c['products'].append(product)
        with open('t1.json', 'w', encoding="utf8") as f:
            json.dump(c, f)
            for i in c['products']:
                print("Название:", i['Название'])
                print("Цена:", i['Цена'])
                print("Вес:", i['Вес'])
                if i['Наличие']:
                    print("В наличии!")
                else:
                    print("Нет в наличии!")
            print(c)
z2()