
candidate_name = []
for x in range(3):
    candidate_name.append(input(" Please insert the name of the candidate "))
# print (candidate_name)

candidate_vote = []
for x in range(3):
    candidate_vote.append(input(" Please insert your vote "))
# print (candidate_vote)

class Person:
    def __init__(self, name, vote):
        self.name = name
        self.vote = vote

    def print_smth(self):
        print (self.name , self.vote)

# c1 = Person("Ankon", 0)
# c1.print_smth()

c01 = Person(candidate_name[0], int(0))
c02 = Person(candidate_name[1], int(0))
c03 = Person(candidate_name[2], int(0))

c04 = [c01, c02, c03]

for x in candidate_vote:
    for y in c04:
        if x in y.name:
            y.vote = y.vote + 1

counter = max(c01.vote, c02.vote, c03.vote)

for x in c04:
    if x.vote >= counter:
        print(x.name)

