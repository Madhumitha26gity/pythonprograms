CH=input("Enter the set to perform:")

if(CH =="X"):
  s1={1.4,2.9,0.8,"madhu",(1,2,3)}
  s2=set([18,20,22])
  o=int(input("Enter the option:"))
  
  if(o==1):  
    print("Displaying the set-1: ",s1)

  if(o==2):
    print("Displaying the set-2: ",s2)

  if(o==3):
    s= input("Enter the set to perform:")
    if(s=='a'):
      a={}
      print("Datatype of a: ",type(a))
    if(s=='b'):
     b=set()
     print("Datatype of b: ",type(b))

  if(o==4):
   s2=set([18,20,22])
   print(s2)
   s2.add("sulo")
   print("Adding element in set-2: ",s2)

  if(o==5):
    s2=set([18,20,22])
    print("Displaying the set-2: ",s2)
    s2.update([47,48,49])
    print("Updating element in set-2: ",s2)

  if(o==6):
   s2.discard(47)
   print("Discarding the given element in set-2: ",s2)

  if(o==7):
    s2.remove(22)
    print("Remove the given element in set-2: ",s2)

  if(o==8):
    s1.clear()
    print("Clearing set-1: ",s1)

elif(CH =="Y"):
  s3 = {1, 2, 3, 4, 5}
  s4 = {4, 5, 6, 7, 8}
  print(s3)
  print(s4)
  o=int(input("Enter the option:"))

  if(o==9):
    print("Union:",s3|s4)
  if(o==10):
    print("Intersection:",s4&s3)
  if(o==11):
    print("Difference:",s3-s4)
  if(o==12):
    print("Symmetric:",s3^s4)                                                                                                                                                                                                                                                                               

  if(o==13):
    s5=s3.copy()
    print("Copying elements of set-3 to set-5:",s5)

  if(o==14):
    print("Whether SET-3 is a disjoint set of SET-4 or not:",s3.isdisjoint(s4))
  
  if(o==15):
    print("Whether SET-3 is a disjoint set of SET-4 or not:",s3.issuperset(s4)) 
  if(o==16):
    print("Whether SET-3 is a subset of SET-4 or not:",s3.issubset(s4)) 
  if(o==17):
    print("popping:",s3.pop()) 
  if(o==18):
    print("maximum:",max(s3))
  if(o==19):
    print("minimum:",min(s3))
  if(o==20):
    print("length:",len(s4))
  if(o==21):
    print("sum of elements:",sum(s4))
  if(o==22):    
    print("Sorted set:",sorted(s4))
  if(o==23):
    for i in set(s4):
      print(i)
else:
  print("INVALID OPTION!")
