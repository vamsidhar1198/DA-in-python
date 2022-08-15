def isbig(x):
    j=0
    for i in x:
        if ord(i)>=65 and ord(i)<=90:
            j+=1
    if j==len(x):return True 
    else: return False 
def issmall(x):
    j=0
    for i in x:
        if ord(i)>=97 and ord(i)<=122:
            j+=1
    if j==len(x):return True
    else: return False
def small(x):
    b=''
    for i in x:
        if ord(i)>=65 and ord(i)<=90:
                b=b+chr(ord(i)+32)
        else: b=b+i
    return b
def big(x):
    b=''
    for i in x:
        if ord(i)>=97 and ord(i)<=122:
                b=b+chr(ord(i)-32)
        else: b=b+i
    return b
def cap(x):
    b=''
    if ord(x[0])>=97 and ord(x[0])<=122: b=b+chr(ord(x[0])-32)
    for i in range(1,len(x)):
        if ord(x[i])>=65 and ord(x[i])<=90: b=b+chr(ord(x[i])+32)
        else: b=b+x[i]
    return b
def swap(x):
    b=''
    for i in x:
        if ord(i)>=97 and ord(i)<=122: b=b+chr(ord(i)-32)
        elif ord(i)>=65 and ord(i)<=90: b=b+chr(ord(i)+32)
        else:b=b+i
    return b
def capslock(x):
    b=''
    if ord(x[0])>=97 and ord(x[0])<=122: b=b+chr(ord(x[0])-32)
    for i in range(1,len(x)):
        if ord(x[i-1])==32:
            if ord(x[i])>=97 and ord(x[i])<=122:b=b+chr(ord(x[i])-32)
            else:b=b+x[i]
        else:
            if ord(x[i])>=65 and ord(x[i])<=90: b=b+chr(ord(x[i])+32) 
            else: b=b+x[i]
    return b
def cou(x,a,sr=0,er=0):
    b=0
    if er==0: er=len(x)
    for i in range(sr,er):
        if x[i]==a:
            b+=1
    return b
def exchange(x,a,b,c=0):
    d=''
    if c==0: c=cou(x,a)
    e=0
    for i in x:
        if i==a:
            if e<c:e+=1;d=d+b
            else:d=d+i
        else:d=d+i
    return d
def lead(x,a,sr=0):
    for i in range(sr,len(x)):
        if x[i]==a:
            break
    return i
def div(x,c=' '):
    a=[]
    b=''
    for i in range(0,len(x)):
        if x[i]==c:
            a=a+[b]
            b=''
            continue
        b=b+x[i]
        if i==len(x)-1:
            a=a+[b]
    return a
def part(x,a=' '):
    b=[]
    for i in range(0,len(x)):
        if x[i]==a:
            
            b=[x[:i]]+[x[i]]+[x[i+1:]]
            break
        elif x[0]==' ':
            b=[' ',' ']+[x[1:]]
            break
        elif a==' ':
            b=[x]+[' ',' ']
            break            
    return b
def isstart(x,a,b=0):
        if x[b]==a:return True
        else:return False
def isend(x,a,b=-1):
    if b==-1:
        b=len(x)-1
    if x[b]==a:return True
    else: return False
def isal(x):
    a=0
    for i in x:
        if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122): a+=1
    if a==len(x):return True
    else:return False
def isnum(x):
    a=0
    for i in x:
        if (ord(i)>=48 and ord(i)<=57): a+=1
    if a==len(x):return True
    else:return False

def isaldigit(x):
    a=0
    b=0
    for i in x:
        if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) : a+=1
        elif (ord(i)>=48 and ord(i)<=57):b+=1
    if a>=1 and b>=1 and (a+b)==len(x):return True
    else:return False
def isgap(x):
    a=0
    for i in x:
        if i==' ':
            a+=1
    if a==len(x):return True
    else: return False
def iscapslock(x):
    b=0
    a=div(x)
    for i in a:
        if ord(i[0])>=65 and ord(i[0])<=90:
            b+=1
    if b==len(a):return True
    else:return False
def take(x,a):
    b=''
    for i in x:
        if i==a:continue
        else:b=b+i
    return b
def trans(x,k='',v=''):
    c=''
    a=[]
    b=[]
    e=0
    if len(k)!=len(v):
        print('give equal number of keys and values')
    for i in k:a=a+[i]
    for i in v:b=b+[i]
    d={}
    for i in range(len(a)): d.update({a[i]:b[i]})
    for j in x:
        for w in d.keys():
            if j==w: 
                c=c+d[w]
                e=e+1
                continue
        if e==0:c=c+j
        e=0
    return c        
        
          
    
    
















