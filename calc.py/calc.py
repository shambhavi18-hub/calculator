

def add(n,m):
    return n+m
def sub(n,m):
    return n-m
def mul(n,m):
    return m*n
def div(n,m):
    return n/m
def mod(n,m):
    return n%m
def power(n,m):
    return n**m
def floor(n,m):
    return n//m

print("---------------------------")
print("       calculator menu     ")
print("---------------------------")
print("1. addition(+)")
print("2. subtraction(-)")
print("3. multiplication(*)")
print("4. division(/)")
print("5. modulus(%)")
print("6. power(**)")
print("7. floor division(//)")
print("---------------------------")
while True :
    try :

        a = float(input("enter a number"))
        print("you entered",a)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    try:
        b = float(input("enter a number"))
        print("you entered",b)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    op = input("enter the operator option (1-7)")
    if(op=="1"):
        result = (add(a,b))
    elif(op=="2"):
        result = (sub(a,b))
    elif(op=="3"):
        result = (mul(a,b))
    elif(op=="4"):
        if(b==0):
            print("division by zero is not allowed")
            continue
        result = (div(a,b))
    elif(op=="5"):
        result = (mod(a,b))
    elif(op=="6"):
        result = (power(a,b))
    elif(op=="7"):
        result = (floor(a,b))
    
        
    
    else :
        print("operator out of option")
        continue
    print("-----------------------------------")
    print(result)
    print("-----------------------------------")
    ask = input("do you want to continue (y/n)")
    print("-----------------------------------")

    if(ask=="n"):
        print("thank you for using the calculator")
        print("-----------------------------------")
        break
    elif(ask=="y"):
        continue
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue

      

    
    
     










