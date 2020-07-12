while True:

    try:
        text = str(input(' Provide the sentence '))
        Letter = 0
        Words = 0
        Sentence = 0
        
        Words=len(text.split())
        
        fakeString = ("".join(text))
        for x in fakeString:
            if (x==".") or (x=="?") or (x=="!"):
                Sentence +=1 

        for y in text:
            if y.isalpha():
                Letter +=1

        L = (100 * Letter)/Words
        S = (100 * Sentence)/ Words
        index = 0.0588 * L - 0.296 * S - 15.8

        roundoff = round(index)


        # print(Letter)
        # print(Words)
        # print(Sentence)
        # print(index)
        print("Grade", roundoff)

        break
    except:
        print("That's not a valid option, please provide String")