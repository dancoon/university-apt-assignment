from person import Person

class Student(Person):
   def __init__(self, first_name='', second_name='', date_left='', age='', date_joined=None, reg_no='', dob=''):
      super().__init__(first_name, second_name, date_left, age, date_joined)  

   def is_studying(self):
      pass