import math, random
from typing import List


# 1- Given a list of numbers, create a function that returns a list where all similar adjacent
# elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
# Note:
# You may create a new list or modify the passed in list.


def question_1(list):
    new_list = []
    for i in range(len(list)):
        j = i + 1
        if j < len(list) and list[i] != list[j]:
            new_list.append(list[i])

    new_list.append(list[-1])
    return new_list


print(question_1([1, 2, 2, 3, 3, 3, 5]))

# 2-​ ​Consider dividing a string into two halves
# Case1:
# The length is even, the front and back halves are the same length.
# Case2:
# The length is odd, we’ll say that the extra char goes in the front half.
# E.g. ‘abced’, the front half is ‘abc’, the back half’de.
# Given 2 strings, a and b, return a string of the form:
# (a-front + b-front) + (a-back +b-back)


def question_2(str_1, str_2):

    (str_1_front, str_1_back) = spilt_str(str_1)
    (str_2_front, str_2_back) = spilt_str(str_2)

    return str_1_front + str_2_front + str_1_back + str_2_back


def spilt_str(str):
    half_str = math.ceil(len(str) / 2)
    first_half = str[:half_str]
    second_half = str[half_str:]

    return (first_half, second_half)


print(question_2("foo", "boo"))

# 3- Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.
# E.X. [1,5,7,9] -> True
# [2,4,5,5,7,9] -> False


def question_3(list):
    check_list = []
    for i in list:
        if i not in check_list:
            check_list.append(i)
        else:
            check_list.remove(i)

    return len(list) == len(check_list)


print(question_3([1, 5, 7, 9]))
print(question_3([2, 4, 5, 5, 7, 9]))
print(question_3([1, 5, 7, 9, 10, 2]))
print(question_3([1, 5, 7, 9, 10, 2, 1]))


# 4- Given unordered list, sort it using algorithm bubble sort
# ( read about bubble sort and try to implement it)


def question_4(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


my_list = [64, 34, 25, 12, 22, 11, 90]
question_4(my_list)
print(my_list)


# 5- Gusses game
# ● Your game generates a random number and gives only 10 tries for the user to
# guess that number.
# ● Get a user input and compare it with the random number
# ● Display a hit message to the user in case the use number is smaller or bigger of
# the random number
# ● If the user type number is out of range(100), display a message that is not allowed
# and don’t count this as try.
# ● If user type a number that has been entered before, display a hint message and
# don’t count this as try
# TODO:
# ● In case the user entered a correct number within the 10 tries, display a
# congratulations message and let your application guess another random number
# with the remain number of tries
# ● If the user finishes all his tries, display a message to ask him if he wants to play
# again or not.


number_allowed_tries = 10
random_number_start = 1
random_number_end = 20
random_number = random.randint(random_number_start, random_number_end)
number_history: List[int] = []
number_current_tries = 0


def question_5():
    # status = ""
    is_guessed = False
    terminate = True
    anwser = ""
    global number_current_tries
    while terminate:
        while number_current_tries < number_allowed_tries:
            is_guessed = find_the_number()
            if is_guessed:
                print("you will play again until you finish your tries")
                global random_number
                random_number = random.randint(random_number_start, random_number_end)
                number_history.clear()
                question_5()
        if not is_guessed:
            print("hard luck")
        anwser = input("try agin?: (y/n): ").lower()
        if anwser == "y" or anwser == "n":
            if anwser == "n":
                terminate = False
            else:
                number_current_tries = 0
                number_history.clear()
        else:
            print("invalid option")


def logging_info(status, input):
    number_history.sort()
    print(
        f"""
        Range of the number: ({random_number_start}, {random_number_end})
        Number of tries: {number_allowed_tries}
        Current tries: {number_current_tries}
        Available treis: {number_allowed_tries - number_current_tries}
        Last input: { input }
        Status: {status}
        History: {number_history}
        """
    )


def find_the_number():
    is_guessed = False
    global number_current_tries
    status = ""
    num = input("guess a number: ")
    if num.isdigit():
        num = int(num)
        if num > random_number_end:
            status = (
                "your number is out of range (this try will not be count), try again."
            )
        elif num in number_history:
            status = "you have entered this number before"
        elif num > random_number:
            status = "the number is bigger"
            number_current_tries += 1
            number_history.append(num)
        elif num < random_number:
            status = "the number is smaller"
            number_current_tries += 1
            number_history.append(num)
        elif num == random_number:
            status = "congratulations you have guess the number"
            logging_info(status, num)
            is_guessed = True
            return is_guessed
    else:
        status = "you have entered an invalid number."

    logging_info(status, num)

    return is_guessed


question_5()
