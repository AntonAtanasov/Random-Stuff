"""
user_input = "A-E-B-C-D"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_input = user_input.replace("-", "")
new_alpha = alphabet
for letter in letter_input:
    new_alpha = new_alpha.replace(letter, "")
print(new_alpha)
print(alphabet)


user_input = "A-E-B-C-D"
letter_input = user_input.replace("-", "")
print(letter_input)
for index in letter_input:
    pass

line = '1234567890'
"""


def split_input(path):
    letter_input = path.replace("-", "")
    n = 2
    print([letter_input[i:i+n] for i in range(0, len(letter_input)-1, 1)])

split_input("A-E-B-C-D")
split_input("A-B-C")
split_input("A-B")
