import random
min_value=1
max_value=6
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are....")
    value1=random.randint(min_value, max_value)
    value2=random.randint(min_value, max_value)
    print(value1,value2)
    roll_again = input("Press 'y' to roll the dices again.")


