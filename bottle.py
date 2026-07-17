class bottle():
    #properties/attributes
    # constructor
    def __init__(self,brand,flavour):
        self.brand=brand
        self.flavour=flavour
        self.size="1 Ltr"

    # Another Function
    def show_details(self):
        print("The details of Product are:")
        print("Brand: "+self.brand)
        print("Flavour: "+self.flavour)
        print("Size: "+self.size)
        
Drink1=bottle("Fanta","orange")
Drink1.show_details()
print("\n\n")
Drink2=bottle("Coca-Cola","classic")
Drink2.show_details()