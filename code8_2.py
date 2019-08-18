import datetime

class Person(object):

    def __init__(self, name):
        """「人間」を生成する"""
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        """selfの名前（フルネーム）を返す"""
        return self.name

    def getLastName(self):
        """selfの姓を返す"""
        return self.lastName

    def setBirthday(self, birthdate):
        """birthdayをdatetime.date型にする
           selfの生年月日をbirthdateと仮定する"""
        self.birthday = birthdate

    def getAge(self):
        """selfの現在の年齢を非単位で返す"""
        if self.birthday==None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """selfの名前がotherの名前と比べて
        　 アルファベット順で前ならばTrueを、
           そうでなければFalesを返す
           比較は、姓について行われるが、
           姓が同じであれば名前（フルネーム）が比較される"""
        if self.lastName==other.lastName:
            return self.name < other.lastName
        return self.lastName < other.lastName

    def __str__(self):
        """selfの名前（フルネーム）で返す"""
        return self.name

class MITPerson(Person):

    nextIdNum = 0 #個人番号の識別

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def isStudent(self):
        return isinstance(self, Student)

    def __lt__(self, other):
        return self.idNum < other.idNum

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

class Grad(Student):
    pass

class TransferStudent(Student):

    def init(self, name, fromSchool):
        MITPerson.__init__(self, mame)
        self.fromSchool = fromSchool

    def getOldSchool(self):
        return self.fromschool

class Grades(object):
    def __init__(self):
        """からの成績ブックを生成する"""
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """studentをStudent型とする
           studentを成績ブックへ追加する"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """gradeをfloat型とする
           gradeをstudentの成績リストへ追加する"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def getGrades(self, student):
        """studentの成績リストを返す"""
        try: #studentの成績リストのコピーを返す
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')

    def getStudents(self):
        """成績ブックに収められた学生のリストを、
           アルファベット順に、一度に１要素ずつ返す"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        #return self.students[:] #学生のリストのコピーを返す
        for s in self.students:
            yield s

def gradeReport(course):
        """courseをGrades型とする"""
        report = ''
        for s in course.getStudents():
            tot = 0.0
            numGrades  =  0
            for g in course.getGrades(s):
                tot += g
                numGrades += 1
            try:
                average = tot/numGrades
                report = report + '\n'+ str(s) + '\'s mean grade is ' + str(average)
            except  ZeroDivisionError:
                report = report + '\n'+ str(s) + ' has no grades'
        return report

"""code8_2 main """
# me = Person('Michaei Guttag')
# him = Person('Barack Hussein Obama')
# her = Person('Madonna')
# print(him.getLastName() )
# him.setBirthday( datetime.date(1961, 8, 4))
# her.setBirthday( datetime.date(1958, 8, 16))
# print(him.getName(),'is',him.getAge(),'days old ')

# pList = [me,him,her]
# for p in pList:
#     print(p)

# pList.sort()
# for p in pList:
#     print(p)

"""code8_3 main """
# p1 = MITPerson('Barbara Beaver')
# print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))
# p1 = MITPerson('Mark Guttag')
# p2 = MITPerson('Billy Bob Beaver')
# p3 = MITPerson('Billy Bob Beaver')
# p4 = Person('Billy Bob Beaver')

"""code8_4 main """
# p5 = Grad('Buzz Aldrin')
# p6 = UG('Billy Beaver', 1984)
# print(p5, 'is a graduate student is', type(p5)==Grad)
# print(p5, 'is an undergraduate student is', type(p5)==UG)

# print(p5, 'is a student is', p5.isStudent())
# print(p6, 'is a student is', p6.isStudent())
# print(p3, 'is a student is', p3.isStudent())

"""code8_6 main """
# ug1 = UG('Jane Doe', 2014)
# ug2 = UG('John Doe' , 2015)
# ug3 = UG('David Henry' , 2003)
# g1 = Grad('Billy BuCkner')
# g2 = Grad('Bucky F. Dent')
# sixHundred = Grades()
# sixHundred.addStudent(ug1)
# sixHundred.addStudent(ug2)
# sixHundred.addStudent(g1)
# sixHundred.addStudent(g2)
# for s in sixHundred.getStudents():
#     sixHundred.addGrade(s,75)
# sixHundred.addGrade(g1,25)
# sixHundred.addGrade(g2,100)
# sixHundred.addStudent(ug3)
# print(gradeReport(sixHundred))

"""code8_8 main """
book = Grades()
book.addStudent(Grad('Julie'))
book.addStudent(Grad('Charlie'))
for s in book.getStudents():
    print(s)

