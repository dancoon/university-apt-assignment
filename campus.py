from university import University

class Campus(University):
    def __init__(self, university_name, population, location, branch_name=''):
        super().__init__(university_name, population, location)
        self.branch_name = branch_name
