class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        grading_scale = {
            (90, 100): 'O',
            (80, 89): 'E',
            (70, 79): 'A',
            (55, 69): 'P',
            (40, 54): 'D',
            (0,  39): 'T'
        }

        average_score = sum(self.scores)/len(self.scores)
        for (low, high), grade in grading_scale.items():
            if low <= average_score <= high:
                return grade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
