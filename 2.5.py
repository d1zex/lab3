import itertools

def print_permutations():
    user_input = input("Enter a string: ")
    permutations = itertools.permutations(user_input)
    
    for perm in permutations:
        print(''.join(perm))

print_permutations()