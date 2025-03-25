class person:
    def __init__(self,name:str,contact_info:str):
        self.name = name
        self.contact_info = contact_info

    # methods
    def update_contact_info(self,new_contact_info:str):
        self.contact_info = new_contact_info
        print(f'Contact info updated for {self.name} \nThe new contact info is: {self.contact_info}')

# For testing only 
# name1 = input("Enter the name of the first person: ")
# contact_info1 = input("Enter the contact info of the first person: ")
# person1 = person(name1, contact_info1)

# name2 = input("Enter the name of the second person: ")
# contact_info2 = input("Enter the contact info of the second person: ")
# person2 = person(name2, contact_info2)

# print(f'Name and contact info: {person1.name}, {person1.contact_info}')
# print(f'Name and contact info: {person2.name}, {person2.contact_info}')

# new_contact_1 = input(f'Enter the new contact info for {name1}:')
# person1.update_contact_info(new_contact_1)
# new_contact_2 = input(f'Enter the new contact info for {name2}:')
# person2.update_contact_info(new_contact_2)

