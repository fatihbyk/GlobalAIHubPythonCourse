class cooking:
    def add_salt(self,number):
        print(f" Please add {number} teaspoon of salt")
    def cooking(self,minute):
        print(f"Please mix the ingredients and cook {minute } minutes")
    def soak_inwater(self,ingredient,minute):
        print(f"Soak the {ingredient} in plenty of water,at least {minute} hours. ")
    def add_water(self,glass):
        print(f"Please add {glass} glass of water")


class HaricotBean(cooking):
    def __init__(self):
        self.soak_inbeans=6
        self.minuteof_cooking=20
        self.glassof_water=3
        self.glassof_liquidoil=3
        self.spoon_tomatopaste=1
        self.onion=1
        self.gramof_haricotbean=500
        self.teaspoonof_salt=1
    def onion_saute(self):
        print("In a separate pan, sauté the onions with tomatopase in liquid oil until soft")
    def slicing(self):
        print(f"Please slice {self.onion} onion")
    def add_ingredients(self):
        print(f"please add {self.gramof_haricotbean} haricotbean")


class Eggplant(cooking):
    def __init__(self):
        self.soak_ineggplant = 1
        self.numberof_eggplant=5
        self.minuteof_cooking = 15
        self.spoon_tomatopaste = 1
        self.glassof_water=1
        self.glassof_liquidoil=3
        self.numberof_tomato=3
        self.onion=1
        self.numberof_tomato = 3
        self.numberof_redpepper=2
        self.numberof_greenpepper =2
        self.teaspoonof_salt=1
    def onion_saute(self):
        print(f"In a separate pan, sauté the onions with tomato paste , red pepper and green pepper in"
              f" {self.glassof_liquidoil}spoon of liquid oil until soft")

    def slicing(self):
        print(f"Please slice {self.onion} onion,{self.numberof_tomato} tomato,{self.numberof_greenpepper}"
              f"green pepper , {self.numberof_redpepper} red pepper and {self.numberof_eggplant} eggplant")
    def add_ingredient(self):
        print(f"please add tomato and eggplant")

class Rice(cooking):
    def __init__(self):
        self.rice_soak=1
        self.minuteof_cooking = 10
        self.glassof_rice=2
        self.glassof_hotwater =2
        self.teaspoonof_salt = 1
        self.spoonof_butter=2
    def melting_butter(self):
        print(f"Please melt{self.spoonof_butter} spoon of butter")
    def add_ingredient(self):
        print(f"Please add {self.glassof_rice} glass of rice ")



class main:
    recipe=str(input("select the recipe you want to see : For Rice please press r,"
              "For Eggplant please press e and For Harricot Bean please press h"
                     "For exit, please press x "))
    if(recipe=='r'):
        r=Rice()
        print("Recipe:\n")
        r.soak_inwater("rice",r.rice_soak)
        r.melting_butter()
        r.add_ingredient()
        r.add_salt(r.teaspoonof_salt)
        r.cooking(r.minuteof_cooking)


        print("Bon Appetit <3")
    elif(recipe=='e'):
        print("Recipe:\n")
        e=Eggplant()
        e.slicing()
        e.soak_inwater("eggplant",e.soak_ineggplant)
        e.onion_saute()
        e.add_ingredient()
        e.add_water(e.glassof_water)
        e.add_salt(e.teaspoonof_salt)
        e.cooking(e.minuteof_cooking)
        print("Bon Appetit <3")
    elif(recipe=='h'):

        h=HaricotBean()
        print("Recipe:\n")
        h.soak_inwater("Beans",h.soak_inbeans)
        h.slicing()
        h.onion_saute()
        h.add_salt(h.teaspoonof_salt)
        h.add_water(h.glassof_water)
        h.cooking(h.minuteof_cooking)
        print("Bon Appetit <3")
    elif(recipe=='x'):
        exit
    else:
        print("please enter a valid letter ")







