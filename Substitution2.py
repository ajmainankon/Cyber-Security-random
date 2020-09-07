from string import ascii_letters

cipher_letters = 'nzghqkcdmyfoialxevtswrupjbNZGHQKCDMYFOIALXEVTSWRUPJB'
trans = str.maketrans(ascii_letters, cipher_letters)

text_to_cipher = input('Text to cipher: ')

ciphered = text_to_cipher.translate(trans)
print(f'Ciphered text: {ciphered}')