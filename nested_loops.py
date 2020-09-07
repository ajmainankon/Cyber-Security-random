

if __name__ == '__main__':
    dic  = {}
    list1 = []
    total_student = int(input("enter number of students"))
    for x in range(total_student):
        dic["name"] = str(input())
        dic["score"] = float(input())
        list1.append(dic["name"])
        list1.append(dic["score"])



    print (list1)
            
    


# d[key, value]


