name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, do you want to walk around it or swim across? Type walk to walk around or swim to swim across: ")

    if answer == "walk":
        break
    elif answer == "swim":
        break
    else:
        print("Not a valid option. You LOSE.")

elif answer == "right":
    print()
else:
    print("Not a valid option. You LOSE.")