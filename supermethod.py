class house:
    def __init__(self):
        print("Constructor of Class A")
        
    oa = 1

class club:
    def __init__(self):
        print("Constructor of Class B")
        
    ob = 2

class spade(house, club):
    def __init__(self):
        super().__init__()
        print("Constructor of Class C")
    oc = 3

obj = spade()
print(obj.oa, obj.ob, obj.oc)