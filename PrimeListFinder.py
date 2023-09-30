#This program upon entering a number will represent the prime that comes in counting order.
#For example entering 2, gives you 3. As 3 is the second prime in counting order.

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def findPrime(n):
    count = 0
    num = 2  
    while count < n:
        if prime(num):
            count += 1
        if count == n:
            return num
        num += 1


n = int(input())
print(findPrime(n))
