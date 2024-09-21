"""
    16.	Write a program to print “HELLO WORLD “using function without using print 
        inside of function. (“HELLO WORLD “must be inside Decorator function) 
"""

def text(name):
  return name

def dec_text(func):
  def inner():
    name="HELLO WORLD"
    print(name)
    return name
  return inner

text = dec_text(text)

text()