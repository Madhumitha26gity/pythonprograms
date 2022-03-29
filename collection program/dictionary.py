colour={1:"red",2:"blue",3:"green",4:"yellow"}
print("Displaying the dictionary:",colour)

print("Datatype:",type(colour))

print("Length of dictionary:",len(colour))

colour[5]="white"
print("Adding of items:",colour)

colour[1]="black"
print("Updating of items:",colour)

del colour[3]
print("Removing of items:",colour)

color=colour.copy()
print("Copying the dictionary:",color)

colour.clear()
print("Removing of all elements:",colour)

print("Displaying only keys:")
for i in color.keys():
  print(i)

print("Displaying only values:")
for i in color.values():
  print(i)

print("Displaying full dictionary using loop:") 
for i,j in color.items():
  print(i,"-",j)

print("Checking whether the item exists or not:")
n=input("Enter the item to check: ")
if color.get(n)==None:
  print("Item does not exists!")
else:
  print("Item exists!")
