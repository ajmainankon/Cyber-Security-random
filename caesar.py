while True:

    try:
        key = int(input(' provide the key in integar '))
        text = input(" provide the text ")
        for count in text:
            if count.isalpha():
                if count.isupper():
                    value = ord(count)
                    ciphervalue = (value - ord("A") + key) %26 + ord ("A")
                    #print(ciphervalue)        
                    cypher = chr(ciphervalue)
                    print (cypher, end ="")
                if count.islower():
                    value2 = ord(count)
                    #print(value2)
                    ciphervalue2 = (value2 - ord("a") + key) %26 + ord ("a")
                    #print(ciphervalue2)        
                    cypher2 = chr(ciphervalue2)
                    print (cypher2, end ="")
            else:
                print (count, end="")
        print()
        break
    except:
        print("That's not a valid option, please provide integer")