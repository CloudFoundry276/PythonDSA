def isPalindrome(strng):
    if len(strng) < 1:
        return True
    else:
        if strng[0] == strng[-1]:
            return isPalindrome(strng[1:-1])
        else:
            return False

print("{} is palindrome: {}".format("awesome", isPalindrome("awesome")))
print("{} is palindrome: {}".format("foobar", isPalindrome("foobar")))
print("{} is palindrome: {}".format("tacocat", isPalindrome("tacocat")))
print("{} is palindrome: {}".format("amanaplanacanalpanama", isPalindrome("amanaplanacanalpanama")))
print("{} is palindrome: {}".format("amanaplanacanalpandemonium", isPalindrome("amanaplanacanalpandemonium")))
