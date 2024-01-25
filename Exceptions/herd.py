# DO NOT CHANGE THE IMPORTS. OTHERWISE THE GRADING IN A+ WONT WORK
import dog
from dogexceptions import ObjectIsNotDogObjectError

class Herd:
    def __init__(self, herd_name):
        self.name = herd_name
        self.members = []

    # New dogs can be added, because the herd is empty first.
    def add_member(self, member):
        '''
        Todo: Before adding a new member to the herd, check if it is a Dog object. If it is not, raise a ObjectIsNotDogObjectError
        Hint: isinstance() can be useful.
        Hint: you may refer to Dog class by doing dog.Dog. (filename.Class-name)
        '''
        if not isinstance(member, dog.Dog):
            raise ObjectIsNotDogObjectError(member)

        self.members.append(member)
       

    def is_member_by_name(self, name):
        for member in self.members:
            if member.get_name() == name:
                return member
        return None


    def print_dogs_status(self, number_just_for_clarifying_printouts):
        print("*", number_just_for_clarifying_printouts, "*")
        for dog in self.members:
            print(dog)
        print("****")





