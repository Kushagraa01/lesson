a=bool(input("Enter the value of 'A': "))
b=bool(input("Enter the value of 'B': "))
c=bool(input("Enter the value of 'C': "))

ans1= a and b
ans2= b or c
ans3= b and c
ans4= ans2 and ans3
final_answer= ans1 or ans4

print(type(a), type(b), type(c))
print(ans1)
print(ans2)
print(ans3)
print(ans4)
print("The final answer is or the value of 'Q' is ", final_answer)