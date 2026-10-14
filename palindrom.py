def isPalindrome(number):

    if number < 0:
        return False

    text = str(number)

    if text == text[::-1]:
        return True
    else:
        return False


# ein paar Tests
print(isPalindrome(8778))
print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(12321))
print(isPalindrome(-101))
