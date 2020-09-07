# for x in range(int(input(5))):
#     name = input()
#     score = float(input())
#     print()



if __name__ == '__main__':
    dic = {}
    s = list()
    for x in range(int(input())):
        name = input()
        score = float(input())
        if score in dic:
            dic[score].append(name)
        else:
            dic[score] = [name]
            print(dic[score])
        if score not in s:
            s.append(score)
            print (s)
    m = min(s)
    s.remove(m)
    m1 = min(s)
    # print (dic[m1])
    dic[m1].sort

    for i in dic[m1]:
        print(i)



