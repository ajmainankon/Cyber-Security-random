def hash(s):
    result = 0
    for c in s:
        result = (result + ord(c) * 3 + 17) % 791
    print (result)

hash ("ofo")