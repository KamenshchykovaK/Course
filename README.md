def is_palindrome(word):
    return word == word[::-1]
user_input = input("Word: ")
if is_palindrome(user_input):
    print("+")
else:
    print("-")
# Task 2
word_list = ['mama', 'papa', 'son']
search_word = input("Search the word:")
if search_word in word_list:
    print('Yes')
else:
    print('No')
# Task3
email = input('Enter Email')
if '@' in email:
    print('yes')
else:
    print('no')
