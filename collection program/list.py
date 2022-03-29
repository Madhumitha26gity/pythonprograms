l=[0,2,4,6,8,"rose","daisy","lotus","poppy","gold","gold"]
m=[18,20,22,47,48,49]
ch=input("Enter List to perform the operation:")
if(ch=="a"):
  print(l)
  o=int(input("Enter your option:"))
  if(o==1):
    l.append(3)
    print("Append:",l)
  if(o==2):
    l.extend([1,"tulips"])
    print("Extend:",l)
  if(o==3):
    l.insert(5,"lily")
    print("Insert:",l)
  if(o==4):
    l.remove("lotus")
    print("Remove:",l)
  if(o==5):
    l.pop(4)
    print("Pop:",l)
  if(o==6):
    l.reverse()
    print("Reverse:",l)
  if(o==7):
    print("Count:")
    print(l.count(("gold")))
  if(o==8):
    print("Length:",len(l)) 
  if(o==9):
    l.clear()
    print("Clear:",l)
elif(ch=="b"):  
  print(m)
  o=int(input("Enter your option:"))
  if(o==10):
    print("Maximum:",max(m))
  if(o==11):
    print("Minimum:",min(m))
  if(o==12):
    m.sort()
    print("Sort:",m)
  if(o==13):
    n=input("Enter the item to check: ")
    if(n==18 or n==20 or n==22 or n==47 or n==48 or n==49):
      print("Index:",m.index(n))
    else:
      print("No index value")
else:
    print("Invalid option")
