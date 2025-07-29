
print("==================")
print("Area Calculator 📐")
print("==================")

while True:
 print("Choose the following")
 print()
 print("1) Triangle")
 print("2) Rectangle")
 print("3) Square")
 print("4) Circle")
 print("5) Quit")

 shape = int(input("Which shape (1-4): "))


 if shape == 1:
    height = int(input("height: "))
    base = int(input("base: "))
    area = (height*base)/2
    print("This area is: ",area)
 elif shape == 2:
    length = int(input("length: "))
    width = int(input("width: "))
    area = length*width
    print("This area is: ",area)
 elif shape == 3:
    side = int(input("side: "))
    area = side**2
    print("This area is: ", area)
 elif shape == 4:
    radius = int(input("radius: "))
    area = 3.14*radius**2
    print("This area is: ",area)
 elif shape == 5:
    print("Byeeee")
    break
 else:
    print("Invalid option")
