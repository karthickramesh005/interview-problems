# Write a code to reverse a number in python :

def reverse(num):
    n = str(num)
    n1 = n[::-1]
    n2 = int(n1)
    return n2
num = int(input("Enter a number : "))

ans = reverse(num)

print("Reverse ",num,"number is : ",ans)
