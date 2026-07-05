

def add(n,m):
    return n+m
def sub(n,m):
    return n-m
def mul(n,m):
    return m*n
def div(n,m):
    return n/m

while True :
    try :

        a = float(input("enter a number"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    try:
        b = float(input("enter a number"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    op = input("enter the operator (+,-,*,/)")
    if(op=="+"):
        result = (add(a,b))
    elif(op=="-"):
        result = (sub(a,b))
    elif(op=="*"):
        result = (mul(a,b))
    elif(op=="/"):
        if(b==0):
            print("division by zero is not allowed")
            continue

        result = (div(a,b))
    
    else :
        print("operator out of option")
        continue
    print(result)

    ask = input("do you want to continue (y/n)")
    

    if(ask=="n"):
        print("thank you for using the calculator")
        break
    elif(ask=="y"):
        continue
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue

      

    
    
     










