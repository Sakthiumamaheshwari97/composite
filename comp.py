h=int(input())
if(h>1):
  for i in range (2,h):
     if(h%i==0):
       print("yes")
       break
  else:
     print("no")
