ch=input("ENTER THE TUPLE TO PERFORM:")

if(ch=="A"):
  Tuple1=('red',11,'yellow',22,'green',33,'blue',44)
  Tuple2=Tuple1*2 
  Tuple3=('white',55)
  tuple5=('madhumitha')
  o=int(input("Enter the option:"))
  if(o==1):
      print(Tuple1)
      print("Datatype:",type(Tuple1))

  if(o==2):
      print(Tuple1)
      print("length:",len(Tuple1))

  if(o==3):
      Tuple2=Tuple1*2 
      print("Repetition: ",Tuple2)

  if(o==4):
     Tuple3=('white',55)
     tuple4=Tuple1+Tuple3
     print("Concatenation:",tuple4)

  if(o==5):
     print(Tuple1[1])

  if(o==6):
      print(tuple5[::-1])

  if(o==7):
      print(tuple4[4:9])

  if(o==8):
      print(Tuple1[2][2:4])

  if(o==9):
      print("Deleting tuple:")
      del Tuple2

if(ch=="B"):
    tuple5=('madhumitha')
    print(tuple5)
    o=int(input("Enter the option:"))
    if(o==10):
      print(tuple5[1:])

    if(o==11):
      print(tuple5[:-5])

if(ch=="C"):
    o=int(input("Enter the option:"))
    if(o==12):
      tupl=(18,20,22,47,48,49)
      print("maximum:",max(tupl))

    if(o==13):
      tupl=(18,20,22,47,48,49)  
      print("minimum:",min(tupl))

    if(o==14):
      tupl=(18,20,22,47,48,49)  
      print("sum:",sum(tupl))

    if(o==15):
      tupl=(18,20,22,47,48,49)  
      print("sorted: ",sorted(tupl))

    if(o==16):
      tupl=(18,20,22,47,48,49)  
      print("reversed:",sorted(tupl,reverse=True))

if(ch=="D"):
    o=int(input("Enter the option:"))
    str="temple city"
    tup=tuple(str)
    if(o==17):
      str="temple city"
      print(type(str))

    if(o==18):
      print(str)
      tup=tuple(str)
      print("Datatype:",type(tup))

    if(o==19):
      print(str)
      tup=tuple(str)
      print("Print last value:",tup[-1])

    if(o==20): 
      print(str)
      tup=tuple(str)
      print("Remove last value:",tup[:-1])
  
    if(o==21):
      print(str)
      tup=tuple(str)
      print("Reverse the tuple:",tup[::-1])
