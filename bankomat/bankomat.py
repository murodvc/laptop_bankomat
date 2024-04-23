"""
[
{
"brand":"Acer",
"RAM":8,
"Pocessor":"Intel Core i5",
"Color":"black"
"Memory":"512Gb"
"Price":"512$"
},
......
.......

]

"""
import uuid

"""
Noutbuk dokoni

1. list laptop
3. price laptop
2. add laptop
4. delete laptop
"""
import json


class Laptop:
    def __init__(self):
        try:
            with open("laptops.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("laptops.json", "w") as f:
                json.dump([], f)
                data = []
        self.laptops = data

    def laptop_list(self):
        for laptop in self.laptops:
            print(
                f"ID:{laptop['id']} name:{laptop['brand']} Processor:{laptop['Processor']} , RAM: {laptop['RAM']}, Memory {laptop['Memory']} color: {laptop['Color']} ")

    def commit(self):
        with open("laptops.json", "w") as f:
            json.dump(self.laptops, f, indent=3)

    def add_laptop(self, brand, ram, mem, color, processor, price):
        laptop = {
            "id": str(uuid.uuid4()),
            "brand": brand,
            "RAM": ram,
            "Processor": processor,
            "Color": color,
            "Memory": mem,
            "Price": price
        }
        self.laptops.append(laptop)
        self.commit()

    def price_laptop(self, h):
        for laptop in self.laptops:
            if h == laptop["id"]:
                print(
                 f"ID:{laptop['id']} Processor:{laptop['Processor']} , RAM: {laptop['RAM']}, Memory {laptop['Memory']} ")
                break
        else:
                print("bunaqa id yoq")

    def delete_laptop(self,d):
        for laptop in self.laptops:
            if d==laptop["id"]:
                    self.laptops.remove(laptop)
                    print("laptop o'chirildi")
            break

        else:
            print(" bunday id li laptop topilmadi ")

        with open("laptops.json", "w") as f:
            json.dump(self.laptops, f, indent=3)


def menu():
    print("""
    1. list laptop
    2. add laptop
    3. price laptop
    4. delete laptop
    5. quit
        """)
    ch = input()
    l1 = Laptop()
    match ch:
        case "1":
            l1.laptop_list()
        case "2":
            brand = input("Brand: ")
            ram = input("Ram: ")
            mem = input("Memory: ")
            color = input("Color: ")
            processor = input("Processor: ")
            price = input("Price: ")
            l1.add_laptop(brand=brand, ram=ram, mem=mem, color=color, price=price, processor=processor)
        case "3":
            h = input("laptopning id sini kiritng: ")
            l1.price_laptop(h=h)
        case "4":
            d = input("laptop id sini kiriting: ")
            l1.delete_laptop(d=d)
            pass
        case "5":
            return
    menu()


if __name__ == '__main__':
     menu()