

def add(n,m):
    return n+m
def sub(n,m):
    return n-m
def mul(n,m):
    return m*n
def div(n,m):
    return n/m

while True :
    a = int(input("enter a number"))
    b = int(input("enter a number"))
    op = input("enter the operator (+,-,*,/)")
    if(op=="+"):
        result = (add(a,b))
    elif(op=="-"):
        result = (sub(a,b))
    elif(op=="*"):
        result = (mul(a,b))
    elif(op=="/"):
        result = (div(a,b))
    else:
        print("operator out of option")
    
    print(result)
    ask = input("do you want to continue (y/n)")
    if(ask=="n"):
        break
    else:
        continue
    
      

    
    
     










