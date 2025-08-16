def countingbit(n):

    count =0
    while (n):
        count +=1
        n >>=1

    return count


num= int(input("Enter a value: "))
print("total bits :",countingbit(num))