def f():
    print ("inside function", s)
s = "I LOVE INDIA"

f()

class Food():
    Hotel = "Non.veg restaurant"
    def __init__(self,rice,cooldrinks):
        self.rice = rice
        self.cooldrinks = cooldrinks
    def Food_type(self):
        print("Food rice", self.rice, "Food cooldrinks", self.cooldrinks)

food1 = Food(rice = "fide rice", cooldrinks = "thumsup")
food1.Food_type()
food1.Hotel