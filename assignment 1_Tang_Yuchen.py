# Name: Yuchen Tang
# Assignment One
# Reference: https://github.com/SAIL-LAB155/TeachingMaterial

import turtle


def task1():
    turtle.setup(900, 400)
    turtle.speed(0)
    colors = ["red", "orange", "green", "blue", "purple"]

    # Square
    turtle.penup()
    turtle.goto(-280, 0)
    turtle.pendown()
    for i in range(12):
        turtle.pencolor(colors[i % 5])
        length = 35 + i * 3
        for j in range(4):
            turtle.forward(length)
            turtle.right(90)
        turtle.right(30)

    # Triangle
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(0)
    turtle.pendown()
    for i in range(12):
        turtle.pencolor(colors[i % 5])
        length = 45 + i * 3
        for j in range(3):
            turtle.forward(length)
            turtle.right(120)
        turtle.right(30)

    # Star
    turtle.penup()
    turtle.goto(280, 0)
    turtle.setheading(0)
    turtle.pendown()
    for i in range(12):
        turtle.pencolor(colors[i % 5])
        length = 55 + i * 3
        for j in range(5):
            turtle.forward(length)
            turtle.right(144)
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
