
a = int(input("A= "))
b = int(input("B= "))
c= int(input("C= "))
def pow_mod(a,b,c):
    res = 1
    for i in range(b):
        res *= a
    return  res%c
print(pow_mod(a,b,c))













'''Question
Power with Modules
You are given A, B and C .
Calculate the value of (A ^ B) % C

Example Input

Input 1:
A = 2 B = 3 C = 3
Input 2:
A = 5 B = 2 C = 4


Example Output

Output 1: 2
Output 2: 1'''