import msvcrt as my_input
from string import ascii_letters

#YTNSHKVEFXRBAUQZCLWDMIPGJO 
#hello
#ehbbq
alphabets_lower = "abcdefghijklmnopqrstuvwxyz"
alphabets_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
map_dict = {}
key_val = 26
word = str(input("\n Enter plain text \n"))
print(" Enter key of ", key_val)

flag = True

while flag:
    inp_list = [] 
    for i in range(key_val):
        inp = my_input.getche().decode("utf-8")
        inp_list.append(inp)
    if len(set(inp_list)) < key_val or (not ''.join(inp_list).isalpha()):
        print(" You entered duplicate items. Enter egain: ")
        flag = True
    else:
        flag = False

cipher_letters = (''.join(inp_list))

for x in word:

    if x.islower():
        for i, letter in enumerate(alphabets_lower):
            map_dict[letter] = i 
    elif x.isupper():
        for i, letter in enumerate(alphabets_upper):
            map_dict[letter] = i 

encoder = list(cipher_letters)

encoded = []
for letter in word:
    my_key = map_dict[letter]
    encoded.append(encoder[my_key])

encoded_text = ''.join(encoded)
print("\n", encoded_text)

