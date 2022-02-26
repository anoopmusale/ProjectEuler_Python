
def isPalindrome(num):
    return str(num) == str(num)[::-1]

maxPalindrome = -1


for j in range(999,99,-1):  #column decrement second
    for i in range(999,99,-1): #row decrements first
        if isPalindrome(i*j) and (i*j) > maxPalindrome:
            maxPalindrome = i*j

print(maxPalindrome)

