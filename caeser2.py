alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
    forReturn = []
    for count in plaintext:
        if count.isalpha():
            value = ord(count)
            #print(value2)
            ciphervalue = (value - ord("a") + k) %26 + ord ("a")
            #print(ciphervalue2)        
            cypher = chr(ciphervalue)
            forReturn.append(cypher)
            
        else:
            print (count, end="")
            
    print ("".join(forReturn))        
    return " ".join(forReturn)
 

encrypt(alphabet, 3)