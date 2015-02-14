__author__ = 'yangbingxi'

class Student(object):

    @property
    def birth(self):
        return self.birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

obj = Student()
obj.birth = 1986
print obj.age