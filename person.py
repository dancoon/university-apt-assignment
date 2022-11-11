class Person():
    def __init__(self, first_name = '', second_name = '',date_left = '', age = '' ,date_joined = None):
        self.first_name = first_name
        self.second_name = second_name
        self.date_joined = date_joined
        self.age = age
        self.date_left = date_left


    def is_present(self):
        pass
    
    def __repr__(self) -> str:
        return self.first_name + "" + self.second_name

