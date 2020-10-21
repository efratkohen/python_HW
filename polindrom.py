
a=3443
s=str(a)
l=len(s)
if l==1:
    print("True")
else:
    half=int(l/2)
    #if (l % 2) == 0: 
    i=0
    j=l
    while i<half:
        if s[i] == s[j-1]:
            if ((l % 2) == 0 and j-i-1==1 or (l % 2) != 0 and j-i-1==2) :
                print(True)
                break
            i=i+1
            j=j-1
        else:
            print("False")
            break
  

