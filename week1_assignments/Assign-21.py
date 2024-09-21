"""
    21. Write a program to build a home. The Home class should define all the attributes of each room in a home. 
        From the Home class create two homes. FirstHome and SecondHome. First home should have an extra study room 
        as a method. SecondHome should have the work_area as an extra method. should use the concept of inheritance.
"""
class Home:
   
   def _init_(self):
       pass
   
   def master_room(self):
       width = 150
       Length = 200
       print("Area of Master Room is", (width * Length))

   def kids_Room(self):
       width = 300
       Length = 200
       print("Area of Kids Room is ", (width * Length))
     
   def living_Room(self):
       width = 500
       Length = 600
       print("Area of Living Room is ", (width * Length))
     
   def family_Room(self):
       width = 150
       Length = 200
       print("Area of Family Room is ", (width * Length))
     
   def kitchen(self):
       width = 400
       Length = 200
       print("Area of Kitchen is ", (width * Length))
     
     
class FirstHome(Home):
   def _init_(self):
       pass
   def new_Study_Room(self):
       width = 100
       Length = 100
       print("Area of New Study Room is ", (width * Length))
     
     
     
class SecondHome(Home):
   def _init_(self):
       pass
 
   def new_work_Area(self):
       width = 100
       Length = 100
       print("Area of New Work Area is ", (width * Length))
     
     
design1 = SecondHome()
 
design1.family_Room()
design1.new_work_Area()
design1.kids_Room()