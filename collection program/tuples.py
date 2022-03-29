o=int(input("Enter the option:"))
Tuple1=('red',11,'yellow',22,'green',33,'blue',44)
if (o==1):
  print(Tuple1)
  print("Datatype",type(Tuple1))

if (o==2):
  print("length:",len(Tuple1))

if (o==3):
   Tuple2=Tuple1*2 
   print("Repetition: ",Tuple2)

if(o==4):
  Tuple3=('white',55)
  tuple4=Tuple1+Tuple3
  print("Concatenation:",tuple4)

if(o==5):
  print(Tuple1[1])

if(o==6):
  tuple5=('madhumitha')
  print(tuple5[1:])

if(o==7):
  print(tuple5[:-5])

if(o==8):
  print(tuple5[::-1])

if(o==9):
  print(tuple5[4:9])

if(o==10):
  print(tuple4[1][4:9])

if(o==11):
  print("Deleting tuple:")
  del Tuple2
  print(Tuple2)

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

if(o==17):
  str="temple city"
  print(type(str))

if(o==18):
  print(str)
  tup=tuple(str)
  print(type(tup))

if(o==19):
  print(tup[-1])

if(o==20): 
  print(tup[:-1])
  
if(o==21):
  print(tup[::-1])

else:
    print("Invalid Option!")
