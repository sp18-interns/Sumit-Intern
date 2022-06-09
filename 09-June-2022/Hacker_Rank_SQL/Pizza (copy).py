import numbers


class Kitchen():
    def __init__(self):
        pass


def create_pizza(name='', size=None, isveg=False, toppings=None, base='', price=0.0):
 
    if toppings is None:
        toppings = []
    if size is None:
        size = {'Diameter': 0.0, 'Label': ''}
    pizza = {
        'Name': name,
        'Size': size,
        'IsVeg': isveg,
        'Toppings': toppings,
        'Base': base,
        'Price': price
    }
    return pizza


def add_toppings(pizza=None, toppings=None):
    if toppings is None:
        toppings = list()
    if pizza is None:
        pizza = dict()
    pizza['Toppings'].append(toppings)
    return pizza


def add_base(pizza=None, base=''):
    if pizza is None:
        pizza = dict()
    pizza['Base'] = base
    return pizza


def pack_pizza(pizza):
 
    if not (isinstance(pizza.get('Size').get('Diameter'), numbers.Number) and pizza.get('Size').get(
            'Diameter') in range(1, 29)):
        raise Exception(f'Invalid Size: "{pizza.get("Size")}". Please enter size in valid range(1-28)')
    return (f"Selecting a box of size {pizza['Size']['Diameter'] + 1}")


def choose_size(pizza):
    size = pizza["Size"]["Diameter"]
    print(f"Pizza Size is : {size}")
    if size == 7:
        pizza["Size"]["Label"] = "Small"
        return pizza["Size"]["Label"]

    elif size in range(9, 11):
        pizza["Size"]["Label"] = "Medium"
        return pizza["Size"]["Label"]

    elif size >= 11:
        pizza["Size"]["Label"] = "Large"
        return pizza["Size"]["Label"]

    elif size >= 13:
        pizza["Size"]["Label"] = "Extra Large"
        return pizza["Size"]["Label"]
    else:
        raise Exception("Invalid Size,Please Enter Size in valid range(1-28)")


def price_pizza(pizza=None):
 
    if pizza is None:
        pizza = dict()
    size = pizza["Size"]["Label"]
    price_toppings = {'cheese burst': 50.0, 'special spices': 40.0, 'extra paneer': 60.0}
    price = 0.0

    if size == 'Small':
        price = 150.0

    elif size == 'Medium':
        price = 200.0

    elif size == 'Large':
        price = 250.0

    elif size == 'Extra Large':
        price = 300.0

    if 'cheese burst' in pizza.get('Toppings'):
        price += price_toppings['cheese burst']
        return price
    elif 'special spices' in pizza.get('Toppings'):
        price += price_toppings['special spices']
        return price
    elif 'extra paneer' in pizza.get('Toppings'):
        price += price_toppings['extra paneer']
        return price
    else:
        return price
