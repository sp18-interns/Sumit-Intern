import numbers


# def create_pizza(name='', size=None, is-veg=False, toppings=None, base='', price=0.0):
def create_car(name='', type_car=None, ispetrol=False, engine=None, wheel='', price=0.0):
    if engine is None:
        engine = []
    if type is None:
        size = {'type': 'hatchback', 'Label': ''}
    car = {
        'Name': name,
        'Size': type,
        'IsPetrol': ispetrol,
        'engine': engine,
        'wheel': wheel,
        'Price': price
    }
    return car
