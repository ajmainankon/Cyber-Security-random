
#should return a ciphertext where each character is XORed with its respective character in key, assuming that plaintext and key is same length
import itertools 


def sxor(s1,s2):    
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

print(sxor("hellooo", "welcome"))

# text = "ho"
# key = "ab"
# for (x,y) in zip(text, key):
#     to_binary  = ''.join(format(ord(x), 'b'))
#     to_binaryK = ''.join(format(ord(y), 'b')) 
#     result = to_binary + to_binaryK
#     print (result) 
#     print (to_binary)
#     print (to_binaryK)
    



# print (to_binaryK)



