from person import person

class librarian(person):
    def __init__(self,name:str,contact_info:str,employee_id:str,):
        super().__init__(name,contact_info)
        self.employee_id = employee_id

    def add_book(self,book:str):
        pass

    def remove_book(self,book:str):
        pass

    def manage_membership(self,member):
        pass