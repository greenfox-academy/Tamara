class Person(object):
    
    def __init__(self, name="Jane Doe", age="30", gender="female"):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print("Hi, I'm {} , a {} year old {}.".format(self.name, self.age, self.gender))

    def get_goal(self):
        print("My goal is: Live for the moment!")


class Student(Person):
    def __init__(self, name="Jane Doe", age="30", gender="female", previous_organization="The School of Life"):
        super().__init()
        self.previous_organization = previous_organization
        self.skipped_days = 0
    
    def get_goal(self):
        print("Be a junior software developer.")
    def introduce(self):
        print("Hi, I'm {}, a {} year old {} from {} who skipped {} days from the course already.".format(set.name, set.age, set.gender, set.previous_organization))
    def skip_days(self, number_of_days): 
        skipped_days += number_of_days


class Mentor(Person):
    def __init__(self, name="Jane Doe", age="30", gender="female", level="intermadiate"):
        super().__init()
        self.level = level

    def get_goal(self):
        print("Educate brilliant junior software developers.")
    def introduce(self):
        print( "Hi, I'm {}, a {} year old {} {} mentor.".format(self.name, self.age, self.gender, self.level))

class Sponsor(Person):
    def __init__(self, name="Jane Doe", age="30", gender="female", company="Google", hired_students="0"):
        super().__init()
        self.company = company
        self.hired_students = hired_students

    def get_goal(self):
        print("Hire brilliant junior software developers.")
    def introduce(self):
        print( "Hi, I'm {}, a {} year old {} who represents {} and hired {} students so far.".format(self.name, self.age, self.gender, self.company, self.hired_students))
    def hire(self):
        self.hired_students += 1

class PallidaClass(object):
    def __init__(self, class_of_name):
        self.class_name = class_name
        self.students = ()
        self.mentors = ()

    def add_student(self): 
        students.add(Student)
    def add_mentor(self): 
        mentors.add(Mentor)
    def info(): 
        print("Pallida className class has len(students) students and len(mentors) mentors.")


#test
people = []

mark = Person('Mark', 46, 'male')
people.append(mark)
jane = Person()
people.append(jane)
john = Student('John Doe', 20, 'male', 'BME')
people.append(john)
student = Student()
people.append(student)
gandhi = Mentor('Gandhi', 148, 'male', 'senior')
people.append(gandhi)
mentor = Mentor()
people.append(mentor)
sponsor = Sponsor()
elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
people.append(elon)
student.skip_days(3)

for i in range(5):
    elon.hire()

for i in range(3):
    sponsor.hire()

for member in people:
    member.introduce()
    member.get_goal()

badass = LagopusClass('BADA55')
badass.add_student(student);
badass.add_student(john);
badass.add_mentor(mentor);
badass.add_mentor(gandhi);
badass.info();