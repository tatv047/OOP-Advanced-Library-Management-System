from person import person

class member(person):
    def __init__(self,name:str,contact_info:str,member_id:str,membership_type:str,books_borrowed:list):
        super().__init__(name,contact_info)
        self.member_id = member_id
        self.membership_type = membership_type
        self.books_borrowed = books_borrowed

    def borrow_book(self,book:str):
        self.books_borrowed.append(book)
        print(f'{self.name} borrowed {book}')

    def return_book(self,book:str):
        self.books_borrowed.remove(book)
        print(f'{self.name} returned {book}')

    def check_borrowed_books(self):
        return self.books_borrowed

member1 = input("Enter the name of the first member: ")
contact_info1 = input("Enter the contact info of the first member: ")

person1 = person(name1, contact_info1)

name2 = input("Enter the name of the second person: ")
contact_info2 = input("Enter the contact info of the second person: ")
person2 = person(name2, contact_info2)

print(f'Name and contact info: {person1.name}, {person1.contact_info}')
print(f'Name and contact info: {person2.name}, {person2.contact_info}')

new_contact_1 = input(f'Enter the new contact info for {name1}:')
person1.update_contact_info(new_contact_1)
new_contact_2 = input(f'Enter the new contact info for {name2}:')
person2.update_contact_info(new_contact_2)