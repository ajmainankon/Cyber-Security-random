if __name__ == '__main__':
    n = int(input(" Please input the number of students "))
    student_marks = {}
    students = {}
    numbers = []
    for x in range(n):
        name = str(input(" input  a name "))
        for y in range(3):
            number = int(input(" input  three numbers "))
            numbers.append(number)
            student_marks[name] = name
            
            
        avg = sum(numbers)/ len(numbers)
        student_marks[number] = number
        
        students["grass"] = student_marks[name]
        students["num"] = student_marks[number]
        print (student_marks[name], avg)
        print (students)
        numbers.clear()
    
    
    
    







    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()