# DO NOT CHANGE THE IMPORTS. OTHERWISE THE GRADING IN A+ WONT WORK
from trick import Trick
from food import Food
from dogexceptions import \
    FeedingDogErrorMissingList,\
    FeedingDogErrorNotFoodObject, \
    FeedingDogErrorObjectInListNotFoodObject, \
    FeedingDogError



class Dog:
    SLEEPY = 0
    HUNGRY = 1
    BORED = 2
    READY = 3

    def __init__(self, name, foods):
        self.name = name
        self.tricks = []
        self.state = Dog.READY
        self.foods = foods       

    def get_name(self):
        return self.name


    def teach_trick(self, trick_name):
        if self.state == Dog.READY or self.state == Dog.BORED:
            new_trick = Trick(trick_name)  
            self.tricks.append(new_trick)  
            self.state = Dog.SLEEPY
            print(self.get_name() + " learned a new trick: " + new_trick.get_name())
        else:  
            print(self.name + " is too " + self.describe_state() + " to learn new tricks.")

  
    def feed(self, food_given):

        '''
        ToDo:
        
        If the food_given received as a parameter is not a Food object, the method should throw the
        FeedingDogErrorNotFoodObject exception. If there is no food list stored for the dog, the method should
        throw the FeedingDogErrorMissingList exception. If, on the other hand, in the dog's food list,
        an item is not a Food object, the method should throw the FeedingDogErrorObjectInListNotFoodObject exception.

        '''
        if not isinstance(food_given, Food):
            raise FeedingDogErrorNotFoodObject
        if not isinstance(self.foods, list) or not self.foods:
            raise FeedingDogErrorMissingList
        if not all(isinstance(food, Food) for food in self.foods):
            raise FeedingDogErrorObjectInListNotFoodObject

        
        for food in self.foods:
                if food_given.get_food_name() == food.get_food_name():
                    print(self.get_name() + " ate " + food_given.get_food_name() + ".")
                    self.state = Dog.BORED
                    return True
                else:
                    print(self.get_name() + " does not like " + food_given.get_food_name() + ".")
                    return False
        

  
    def sleep(self):
        if self.state == Dog.SLEEPY:
            print(self.name + " had a nice nap.")
            self.state = Dog.HUNGRY
        else:
            print(self.name + " is not sleepy!")

  
    def describe_state(self):
        if self.state == Dog.SLEEPY:
            return "sleepy"
        elif self.state == Dog.HUNGRY:
            return "hungry"
        elif self.state == Dog.BORED:
            return "bored"
        elif self.state == Dog.READY:
            return "ready for actions"
        else:
            return "unknown"

   
    def list_tricks(self):
        list_of_trics = ""
        for trick in self.tricks:
            list_of_trics += trick.get_name() + ", "
        return list_of_trics


    def how_many_tricks(self):
        return len(self.tricks)


    def can_more_tricks(self, other_dog):
        return self.how_many_tricks() >= other_dog.how_many_tricks()


    def __str__(self):
        if len(self.tricks) > 0:
            new_str = self.name + " is "
            new_str += self.describe_state() + " and it can following tricks: "
            new_str += self.list_tricks()
            new_str += "and it is a good dog!"
            return new_str
        else:
            return self.name + " is " + self.describe_state() +"."