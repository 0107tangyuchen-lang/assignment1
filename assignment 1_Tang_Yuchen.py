# Name: Yuchen Tang
# Assignment One
# Reference: https://github.com/SAIL-LAB155/TeachingMaterial

import turtle


def task1():
    print("1. Square")
    print("2. Triangle")
    print("3. Star")
    print("4. Colourful patterns")
    shape = input("Choose 1, 2, 3 or 4: ")

    if shape not in ["1", "2", "3", "4"]:
        print("Please choose 1, 2, 3 or 4.")
        return

    turtle.setup(900, 400)
    turtle.speed(0)

    if shape == "1":
        turtle.penup()
        turtle.goto(-75, 75)
        turtle.pendown()
        for i in range(4):
            turtle.forward(150)
            turtle.right(90)

    elif shape == "2":
        turtle.penup()
        turtle.goto(-90, 60)
        turtle.pendown()
        for i in range(3):
            turtle.forward(180)
            turtle.right(120)

    elif shape == "3":
        turtle.penup()
        turtle.goto(-100, 30)
        turtle.pendown()
        for i in range(5):
            turtle.forward(200)
            turtle.right(144)

    elif shape == "4":
        colors = ["red", "orange", "green", "blue", "purple"]

        # Square pattern
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        for i in range(12):
            turtle.pencolor(colors[i % 5])
            length = 35 + i * 3
            for j in range(4):
                turtle.forward(length)
                turtle.right(90)
            turtle.right(30)

    turtle.hideturtle()
    turtle.done()


def task2():
    print("Ask about hku, robot, jetson, ai or human.")
    print("Enter bye to stop.")

    while True:
        question = input("Question: ").lower()
        words = question.replace("?", "").replace("!", "").replace(".", "").split()

        if question.strip() == "bye":
            break
        elif "hku" in words:
            print("HKU is The University of Hong Kong.")
        elif "robot" in words:
            print("A robot is a machine that can do tasks.")
        elif "jetson" in words:
            print("Jetson is an NVIDIA computer for AI projects.")
        elif "ai" in words:
            print("AI means artificial intelligence.")
        elif "human" in words:
            print("A human is a person.")
        else:
            print("Sorry, I do not know.")


def task3():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Choose +, -, * or /: ")

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("Result:", num1 / num2)
    else:
        print("Invalid operator.")


print("1. Turtle drawing")
print("2. QA bot")
print("3. Calculator")
choice = input("Choose 1, 2 or 3: ")

if choice == "1":
    task1()
elif choice == "2":
    task2()
elif choice == "3":
    task3()
else:
    print("Please choose 1, 2 or 3.")
