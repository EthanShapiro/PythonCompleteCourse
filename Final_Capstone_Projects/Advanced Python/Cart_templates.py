from string import Template

class MyTemplate(Template):
    delimiter = '#'

def Main():
    cart = list()
    cart.append(dict(item="Coke", price=8, qty=2))
    cart.append(dict(item="Cake", price=12, qty=1))
    cart.append(dict(item="Fish", price=32, qty=4))

    # Use delimiter twice $$ to esca[e ot
    t = MyTemplate("#qty x #item = #price")

    total = 0
    print("Cart:")
    for item in cart:
        print(t.substitute(item))
        total += item["price"]
    print("Total:" + str(total))

if __name__ == "__main__":
    Main()
