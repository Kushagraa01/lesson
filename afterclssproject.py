a=int(input("Enter the value of 'A': "))
b=int(input("Enter the value of 'B': "))
c=int(input("Enter the value of 'C': "))

ans1= a & b
ans2= b | c
ans3= b & c
ans4= ans2 & ans3
final_answer= ans1 | ans4

print("The final answer is or the value of 'Q' is ", final_answer)