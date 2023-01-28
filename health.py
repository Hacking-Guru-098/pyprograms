# health management system

from tools import gd,log_exercise,log_food,view_exercise,view_food

# def start():
food=str()
exercise=str()

while True:
    name=input("enter the name :")
    if name=="gaurav":
        open("exercise 1.txt","w")
        open("food 1.txt","w")
        exercise="exercise 1.txt"
        food="food 1.txt"
    elif name=="bhrigu":
        open("exercise 2.txt","w")
        open("food 2.txt","w")
        exercise="exercise 2.txt"
        food="food 2.txt"
    elif name=="sahil":
        open("exercise 3.txt","w")
        open("food 3.txt","w")
        exercise="exercise 3.txt"
        food="food 3.txt"
    else:
        print("invalid input")

    print("press-------------------\n1)log the data:\n2)view the data:\n3)exit:")
    n=int(input())

    if n==1:
        print("1)food:\n2)exercise:")
        x=int(input())
        if x==1:
            log_food(food,name)
        elif x==2:
            log_exercise(exercise,name)
        else:
            print("invalid input:")
    elif n==2:
        print("1)food:\n2)exercise:")
        y=int(input())
        if y==1:
            view_food(food)
        elif y==2:
            view_exercise(exercise)
        else:
            print("invalid input:")
    elif n==3:
        print("bye")
        exit()
    else: 
        print("invalid input!!")
        exit()
