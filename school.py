class School():
    def __init__(self, name = None, students = {}):
        self.name = name
        self.students = students
    def roster(self):
        return self.students
    def add_student(self, student, grade = None):
        if grade in list(self.students.keys()):
            students_in_grade = self.students[grade]
            students_in_grade.append(student)
            updated_list = {grade : students_in_grade}
            self.students.update(updated_list)
        else:
            students_in_grade = []
            students_in_grade.append(student)
            updated_list = {grade : students_in_grade}
            self.students.update(updated_list)
    def grade(self, grade):
        return self.students[grade]
    def sort_roster(self):
        keys = list(self.students.keys())
        for key in keys:
            unordered = self.students[key]
            ordered = sorted(unordered)
            alphabetized = {key : ordered}
            self.students.update(alphabetized)
        return self.roster()