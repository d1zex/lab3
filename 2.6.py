def reverse_sentence():
    user_input = input("Enter a sentence for reversing it: ")
    words = user_input.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)

result = reverse_sentence()
print(result)