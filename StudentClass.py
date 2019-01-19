class Student:

    def __init__(self, rno, name, marks):
        self.rno = rno
        self.name = name
        self.marks = marks
    
    def display(self):
        print('{} {} {}'.format(self.rno, self.name, self.marks))


class School:

    def __init__(self, students):
        self.students = students
    
    def display_all(self):
        for stu in self.students:
            stu.display()

    def display_topper(self):
        topper = self.students[0]
        for s in self.students:
            if topper.marks < s.marks:
                topper = s
        topper.display()

    def get_average_marks(self):
        sum = 0
        for stu in self.students:
            sum += stu.marks
        avg = sum / len(self.students)
        return avg

    def is_below_avg(self, stu):
        avg = self.get_average_marks()

        if stu.marks < avg:
            print('{} is below average'.format(stu.name))
        elif stu.marks == avg:
            print('{} is equal to average'.format(stu.name))
        else:
            print('{} is above average'.format(stu.name))


stu1 = Student(1, 'Heena', 90)
stu2 = Student(2, 'Madhur', 80.4)
stu3 = Student(3, 'Rupali', 70.65)
stu4 = Student(4, 'Varun', 56.98)

school = School([stu1, stu2, stu3, stu4])
school.display_all()

school.display_topper()

school.is_below_avg(stu1)
school.is_below_avg(stu2)
school.is_below_avg(stu3)
school.is_below_avg(stu4)

