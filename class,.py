Text = input("Enter a word: ")

reversed_word = Text[::-1]
print("Reversed word:", reversed_word)

if Text == reversed_word:
    print("This is a palindrome!")
else:
    print("This is not a palindrome.")
