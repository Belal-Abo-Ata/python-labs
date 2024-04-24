# 1- Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.


def question_1(first_name, last_name):
    print(f"{last_name} {first_name}")


question_1("Belal", "Abo Ata")

# 2- Write a Python program that accepts an integer (n) and computes the value of
# n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615


def question_2(n):
    n = str(n)
    return int(n) + int(n + n) + int(n + n + n)
    # Another Solution
    num1 = n
    num2 = n * 10 + n
    num3 = n * 100 + n * 10 + n
    return num1 + num2 + num3


print(question_2(5))

# 3- Write a Python program to print the following here document.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example


def question_3():
    print(
        """ Sample string :
        a string that you "don't" have to escape
        This
        is a ....... multi-line
        heredoc string --------> example
        """
    )


question_3()


# 4- Write a Python program to get the volume of a sphere with radius 6.


def question_4(r=6):
    return 4 / 3 * 3.14 * r**3


print(question_4())


# 5- Write a Python program that will accept the base and height of a triangle and compute
# the area.


def question_5(base, height):
    return 0.5 * base * height


print(question_5(5, 10))

# 6- Write a Python program to construct the following pattern, using a nested for loop.
# Search about method
# end=””
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


def question_6():
    # refactor this code to use only one loop
    for i in range(1, 10):
        if i <= 5:
            print("*" * i)
        else:
            print("*" * (10 - i))


question_6()


# 7- Write a Python program that accepts a word from the user and reverse it.


def question_7(word):
    return word[::-1]


print(question_7("Belal"))


# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.


def question_8():
    for i in range(7):
        if i != 3 and i != 6:
            print(i)


question_8()


# 9-Write a Python program to get the Fibonacci series between 0 to 50


def question_9(end=50):
    start = 0
    aftar_start = 1
    fibonacci = 0
    print(start, aftar_start, end=", ")
    while fibonacci <= 50:
        fibonacci = start + aftar_start
        print(fibonacci, end=", ")
        (start, aftar_start) = (aftar_start, fibonacci)
    print()


question_9()

# 10- Write a Python program that accepts a string and calculate the number of digits and
# letters.


def question_10(word):
    count = 0
    for ch in word:
        if ch.isdigit():
            count += 1

    print(count)


question_10("b12c53ahm")
