"""
    24. write a menu driven python program to create recipes. Once one recipe is done then the quantity of the items 
        in pantry should also be reduced
"""

pantry = {
  "chicken": 500,
  "lemon": 2,
  "cumin": 24,
   "paprika": 18,
   "chilli_powder": 7,
   "yogurt": 300,
   "oil": 450,
   "onion": 5,
   "garlic": 9,
   "ginger": 2,
   "tomato_puree": 125,
   "almonds": 75,
   "rice": 500,
   "coriander": 20,
   "lime": 3,
   "pepper": 8,
   "egg": 6,
   "pizza": 2,
   "spam": 1,
   "beans":1,
   "bread":2,
   "malt_vinegar":1,
   "salt":100,
   "potatoes":2,
   "butter":1,
   "tin_operator":1,
   "spoon":1,
}
 
recipes = {
   "Butter chicken": [
       "chicken",
       "lemon",
       "cumin",
       "paprika",
       "chilli powder",
       "yogurt",
       "oil",
       "onion",
       "garlic",
       "ginger",
       "tomato puree",
       "almonds",
       "rice",
       "coriander",
       "lime",
   ],
   "Chicken and chips": [
       "chicken",
       "potatoes",
       "salt",
       "malt vinegar",
   ],
   "Pizza": [
       "pizza",
   ],
   "Egg sandwich": [
       "egg",
       "bread",
       "butter",
   ],
   "Beans on toast": [
       "beans",
       "bread",
   ],
   "Spam a la tin": [
       "spam",
       "tin opener",
       "spoon",
   ],
}
 
def p_beans_on_toast():
   bean = pantry.get("beans")
   bread = pantry.get("bread")
   print("The beans on toast is ready for serving")
   pantry["beans"] -= 1
   pantry["bread"] -= 1
 
def p_butter_chicken():
   chicken = pantry.get("chicken")
   lemon = pantry.get("lemon")
   cumin = pantry.get("cumin")
   paprika = pantry.get("paprika")
   chilli_powder = pantry.get("chilli_powder")
   yogurt = pantry.get("yogurt")
   oil = pantry.get("oil")
   onion = pantry.get("onion")
   garlic = pantry.get("garlic")
   ginger = pantry.get("ginger")
   tomato_puree = pantry.get("tomato_puree")
   almonds = pantry.get("almonds")
   rice = pantry.get("rice")
   coriander = pantry.get("coriander")
   lime = pantry.get("lime")
   print("The recipes used are : chicken,lemon,cumin,paprika,chilli_powder,yogurt,oil,onion,garlic,ginger,tomato_puree,almonds,rice,coriander and lime")
   print("The butter chicken is ready for serving")
 
   pantry["chicken"] -= 300
   pantry["lemon"] -= 2
   pantry["cumin"] -= 24
   pantry["paprika"] -= 18
   pantry["chilli_powder"] -= 7
   pantry["yogurt"] -= 300
   pantry["oil"] -= 450
   pantry["garlic"] -= 9
   pantry["ginger"] -= 2
   pantry["tomato_puree"] -= 125
   pantry["almonds"] -= 75
   pantry["rice"] -= 500
   pantry["coriander"] -= 20
   pantry["lime"] -= 3
     
def chicken_and_chips():
   chicken = pantry.get("chicken")
   potatoes = pantry.get("potatoes")
   salt = pantry.get("salt")
   malt_vinegar = pantry.get("malt_vinegar")
 
   print("The recipes used are : chicken, potatoes, salt and malt_vinegar")
 
   print("The chicken and chips ready for serving")
 
   pantry["chicken"] -= 200
   pantry["potatoes"] -= 2
   pantry["salt"] -= 100
   pantry["malt_vinegar"] -= 1
 
def pizza_cook():
   pizza = pantry.get("pizza")  
   print("The recipes used is : Pizza")
   print("The pizza is ready for serving")
   pantry["pizza"] -= 2
 
def egg_sandwich():
   egg = pantry.get("egg")
   bread = pantry.get("bread")
   butter = pantry.get("butter")
   print("The recipes used are : egg, bread and butter")
   print("The egg sandwich is ready for serving")
   pantry["egg"] -= 6
   pantry["bread"] -=1
   pantry["butter"] -= 1
 
def spam_a_la_tin():
   spam = pantry.get("spam")
   opener = pantry.get("tin_operator")
   spoon = pantry.get("spoon")
   print("The recipes used are : spam, tin_operator and spoon")
   print("The Spam a la tin is ready for serving")
   pantry["spam"] -= 1
   pantry["tin_operator"] -=1
   pantry["spoon"] -= 1
 
choose = int(input("Enter which item you need to make\n1-Butter Chicken\n2-Chicken and chips\n3-Pizza\n4-Egg Sandwich\n5-Bean on toast\n6-Spam a la tin"))
   
match choose:
   case 1:
       p_butter_chicken()  
       print("The current availble item in pantry is:", pantry)
   case 2:
       chicken_and_chips()
       print("The current available item in pantry is:\n", pantry)
   case 3:
       pizza_cook()
       print("The current available item in pantry is:\n", pantry)
   case 4:
       egg_sandwich()
       print("The current available item in pantry is:\n", pantry)
   case 5:
       p_beans_on_toast()
       print("The current available item in pantry is:\n", pantry)
   case 6:
       spam_a_la_tin()
       print("The current available item in pantry is:\n", pantry)
   case default:
       print("Please choose the correct one recipe")