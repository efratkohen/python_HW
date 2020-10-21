def polindrom(a):
    l=len(a)
    if l==1:
        return True
    else:
        half=int(l/2) 
        i=0
        j=l
        while i<half:
            if a[i] == a[j-1]:
                if ((l % 2) == 0 and j-i-1==1 or (l % 2) != 0 and j-i-1==2) :
                    return True
                i=i+1
                j=j-1
            else:
                return False
def check_palindrome (a):
    sa=str(a)
    s4=sa[2:]
    a5=a+1
    s5=str(a5)
    s55=s5[1:]
    mid=a5+1
    smid=str(mid)
    ssmid=smid[1:5]
    final=mid+1
    sfinal=str(final)
    if (polindrom(s4)and polindrom(s55) and polindrom(ssmid) and polindrom(sfinal)):
        print(a)
    else:
        

 a=int(198888)
 check_palindrome(a)
