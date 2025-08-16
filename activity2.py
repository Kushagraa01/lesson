num1=int(input("Enter the value : "))

def even_odd(n):
    if(n ^ 1 == n+1):
        return True
    else:
        return False


if even_odd(num1):
    print( num1 ,"is even number")
else:
    print( num1 ,"is odd number")