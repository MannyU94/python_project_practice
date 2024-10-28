
def get_digit():
    while True:
        n = (input("What digit of the fibonacci do you want to know? 1-20"))
        if n.isdigit():
            n = int(n)
        else:
            print('Input is not numeric... Try Again!')
            continue

def F(n):
    while True:
        if n <= 1:
            return n
        else:
            return F(n-1) + F(n-2)
    
get_digit()
print(f"The {n}th digit of the fibonacci sequence is", F(n))
print("************************************")


'''
x = 0
y = 1

print(x)
print(y)

for fib in range(20):
    newFib = x + y
    x = y
    y = newFib
    print(newFib)
'''