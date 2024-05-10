class StudentManagement:
    def __init__(self):
        self.students = []

    def create(self, name, roll_no, id,emailid):
        student = {'name': name, 'roll_no': roll_no, 'id': id,'emailid':emailid}
        self.students.append(student)

    def read(self):
        for student in self.students:
            print(student)

    def update(self, id, name=None, roll_no=None,emailid=None):
        for student in self.students:
            if student['id'] == id:
                if name:
                    student['name'] = name
                if roll_no:
                    student['roll_no'] = roll_no
                if emailid:
                    emailid['emailid']=emailid

    def delete(self, id):
        self.students = [student for student in self.students if student['id'] != id]


sm = StudentManagement()
sm.create('raj', 1, '344','d324@gmail.com')
sm.create('jhon', 3, '243','2wd@gmail.com')
sm.create('jay', 2, '278','a3duwn@gmail.com')
print("After creation:")
sm.read()
sm.update('243', name='jhony')
print("After update:")
sm.read()
sm.delete('278')
print("After deletion:")
sm.read()