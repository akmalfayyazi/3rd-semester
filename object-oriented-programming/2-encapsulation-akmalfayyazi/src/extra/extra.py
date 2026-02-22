class Student:
    def __init__(self, first_name, last_name, student_id, grades):
        self._first_name = first_name if first_name else 'Unknown'
        self._last_name = last_name if last_name else 'Unknown'
        self._student_id = student_id if student_id else 'Unknown'
        self._grades = grades

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, name):
        self._first_name = name if name else 'unknown'

    @property
    def last_name(self):
        return self._first_name
    
    @last_name.setter
    def last_name(self, name):
        self._last_name = name if name else 'unknown'
    
    @property
    def student_id(self):
        return self._student_id
    
    @student_id.setter
    def student_id(self, id):
        self._student_id = id if id else 'unknown'
    
    @property
    def grades(self):
        return list(self._grades)

    def get_average(self) -> float:
        return sum(self._grades) / len(self._grades)
    
    def get_highest(self):
        return max(self._grades)

    def get_lowest(self):
        return min(self._grades)
    
    def is_passing(self, threshold= 60.0) -> bool:
        return self.get_average() >= threshold

if __name__ == '__main__':
    stud1 = Student('akmal', 'fayyazi', '2112', [73, 43, 100])
    print(stud1.get_average())
    print(stud1.get_highest())
    print(stud1.is_passing())