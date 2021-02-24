class Pizza:
    price = 15

    def __init__(self, name, ingredinete):
        # print('pizza.__init__', name, ingredinete)
        self.name = name
        self.ingredinete = ingredinete

if __name__ == '__main__':
    print(Pizza.price)

    my_pizza = Pizza('margerita', ['a', 'b', 'c'])
    print(my_pizza)
    print(my_pizza.name)
    print(my_pizza.ingredinete)
    print(my_pizza.price)


