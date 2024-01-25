'''
Todo: Implement the Exception classes ObjectIsNotDogObjectError and FeedingDogError.

ObjectIsNotDogObjectError should get the incorrect 'member'
tried to add. It needs to check which type it is, and tell the type in the message.

FeedingDogError is a superclass for its inheritors FeedingDogErrorMissingList, FeedingDogErrorNotFoodObject
and FeedingDogErrorObjectInListNotFoodObject.
'''

'''
Check the definitons of the classes from the exercise on A+
'''


class ObjectIsNotDogObjectError(Exception): 
    def __init__(self, member): #Creates a new NoDogObjectError object, and stores the received parameter, i.e., the object that was tried to be set as a new member. Also stores information about the type of the wrong object, as well as a message in the form: f"****** Exception: The object ({self.member}) you tried adding in the herd is not a dog object, but an object of {self.type}"
       self.member = member
       self.type = type(member)
       member_str = repr(member)
       self.message = f"****** Exception: The object ({member_str}) you tried adding in the herd is not a dog object, but an object of {self.type}"
    def __str__(self):
        return self.message



class FeedingDogError(Exception): #The purpose of this exception class is just to act as a superclass for its inheritors FeedingDogErrorMissingList, FeedingDogErrorNotFoodObject and FeedingDogErrorObjectInListNotFoodObject. Meaning, this class is not intended to be thrown in other files. This class inherits from the Exception superclass. Write the class to the given file dogexceptions.py
    def __init__(self, msg=""): #TODO Creates a new FeedingDogError object and stores the value received as a parameter in its msg field. As default the msg field is an empty string. This can be done by setting msg="" inside the parenthesis in the init.
        self.msg = msg
    
    def __str__(self):
        return self.msg


class FeedingDogErrorMissingList(FeedingDogError):
    def __init__(self):
        super().__init__()
        self.msg = "****** Exception: Dog object does not have a list of foods"


class FeedingDogErrorNotFoodObject(FeedingDogError):
    def __init__(self):
        super().__init__()
        self.msg = "****** Exception: The object with which the dog is tried to be fed is not a food object"


class FeedingDogErrorObjectInListNotFoodObject(FeedingDogError):
    def __init__(self):
        super().__init__()
        self.msg = "****** Exception: An object in dog's foodlist is not a food object"
