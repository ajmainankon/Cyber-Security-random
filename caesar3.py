alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
   pass # do stuff and return ciphertext
   cipher=''

   for i in plaintext:
       position= alphabet.index(i, 0, len(alphabet))
       newposition=(position+k)%(len(alphabet))
       newchar=alphabet[newposition]
       cipher+=newchar
   print (cipher) 
   return cipher

encrypt(alphabet,3)