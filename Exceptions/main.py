from dog import Dog     # DO NOT CHANGE THE IMPORTS. OTHERWISE THE GRADING IN A+ WONT WORK
from food import Food   # DO NOT CHANGE THE IMPORTS. OTHERWISE THE GRADING IN A+ WONT WORK
from herd import Herd   # DO NOT CHANGE THE IMPORTS. OTHERWISE THE GRADING IN A+ WONT WORK
from dogexceptions import ObjectIsNotDogObjectError, FeedingDogError    # DO NOT CHANGE THE IMPORTS. OTHERWISE THE GRADING IN A+ WONT WORK


def add_dog(herd, dog):
    try:
        herd.add_member(dog)
    except ObjectIsNotDogObjectError as e:
        print(e)


def feed_dog(dog, food):
    try:
        dog.feed(food)
    except FeedingDogError as e:
        print(e)


def main():
    sausages = Food("sausages")
    cookies = Food("cookies")

    dog1 = Dog("Skye", [cookies, sausages])         # Correct
    dog2 = Dog("Chase", "food")                     # List missing
    dog3 = Dog("Marshall", [cookies, "sausages"])   # List has incorrect elements
    dog4 = "Peter"

    dogs = [dog1, dog2, dog3, dog4]

    my_herd = Herd("P. P.")

    for dog in dogs:
        add_dog(my_herd, dog)

    dog1.feed(cookies)                                 # This one should work

    #dog1.feed("carrot")                              # This one should cause a FeedingDogErrorNotFoodObject when commented out
    #dog2.feed(cookies)                               # This one should cause a FeedingDogErrorMissingList when commented out
    #dog3.feed(sausages)                              # This one should cause a FeedingDogErrorObjectInListNotFoodObject when commented out

    dogs = [dog1, dog2, dog3]
    foods = ["carrot", cookies, sausages]

    for i in range(3):
        feed_dog(dogs[i], foods[i])
        

if __name__ == "__main__":
    main()
