def get_array(arr):
  size = int(input("enter the size of array"))
  print("emter "+str(size)+"elements:")
  for i in range(size):
    element = input()
    arr.append(element)

def display_array(arr):
  print("array is:"+"["+arr+"]")

def main():
  arr = []
  get_array(arr)
  display_array(arr)
  
main()

