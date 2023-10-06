
def palindrome(s):
    value_s = s.replace(" ", "").lower()
    return value_s == value_s[::-1]
string = input("Enter a string: ")
if palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
