from person import Person

class Lecturer(Person):
    def __init__(self, first_name='', second_name='', date_left='', age='', date_joined=None, employee_id= '', marital_status ='', salary = ''):
        super().__init__(first_name, second_name, date_left, age, date_joined)
    
    def is__teaching(self):
        pass

