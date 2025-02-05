def is_palindrome(s):
    normalized_str = ''.join(s.split()).lower()
    return normalized_str == normalized_str[::-1]

print(is_palindrome("madam"))