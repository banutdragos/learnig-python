# 4.1 Assign the value 7 to the variable guess_me. Then, write the conditional tests (if,
# else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if
# greater than 7, and 'just right' if equal to 7.
guess_me = 7
while True:
    guessed = int(input('Guess the number:'))
    if guessed == guess_me:
        print("Grats'! You guessed the number!!!")
        break
    elif guessed < guess_me:
        print("Sorry! The number is higher\nTry again!")
    else:
        print("Sorry! The number is lower\nTry again!")
print()


# 4.2 Assign the value 7 to the variable guess_me and the value 1 to the variable start.
# Write a while loop that compares start with guess_me. Print too low if start is less
# than guess me. If start equals guess_me, print 'found it!' and exit the loop. If
# start is greater than guess_me, print 'oops' and exit the loop. Increment start at
# the end of the loop.


# 4.3 Use a for loop to print the values of the list [3, 2, 1, 0].
print("4.3 Use a for loop to print the values of the list [3, 2, 1, 0].")
for number in list(range(3, -1, -1)):
    print(number)
print()


# 4.4 Use a list comprehension to make a list of the even numbers in range(10).
print("4.4 Use a list comprehension to make a list of the even numbers in range(10).")
comp_list = [number for number in range(10) if number % 2 == 0]
print(f"Here is the list: {comp_list}\n")


# 4.5 Use a dictionary comprehension to create the dictionary squares. Use range(10)
# to return the keys, and use the square of each key as its value.
print("4.5 Use a dictionary comprehension to create the dictionary squares.")
comp_dict = {number: number ** 2 for number in range(10)}
print(f"Here is the dictionary: {comp_dict}\n")


# 4.6 Use a set comprehension to create the set odd from the odd numbers in
# range(10).
print("4.6 Use a set comprehension to create the set odd from the odd numbers in range(10).")
comp_set = {number for number in range(10) if number % 2 != 0}
print(f"Here is the set: {comp_set}\n")

# 4.7 Use a generator comprehension to return the string 'Got ' and a number for the
# numbers in range(10). Iterate through this by using a for loop.
print("4.7 Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10).")
for number in range(10):
    print(f"Got {number}")
print()


# 4.8 Define a function called good that returns the list ['Harry', 'Ron', 'Hermione'].
def good():
    return ['Harry', 'Ron', 'Hermione']


# 4.9 Define a generator function called get_odds that returns the odd numbers from
# range(10). Use a for loop to find and print the third value returned.
print("4.9 Define a generator function called get_odds that returns the odd numbers from"
      " range(10). Use a for loop to find and print the third value returned.")


def get_odds(i):
    odds = [num for num in range(10) if num % 2 != 0]
    return odds[i]


for index in range(10):
    if index == 2:
        print(get_odds(index))
print()

# 4.10 Define a decorator called test that prints 'start' when a function is called and
# 'end' when it finishes.
print("4.10 Define a decorator called test that prints 'start' when a function is called and 'end' when it finishes.")


def deco(func):
    print("Start")
    func()
    print("End")


@deco
def testdeco():
    print("inside")


# testdeco()
print()

# 4.11 Define an exception called OopsException. Raise this exception to see what hap‐
# pens. Then write the code to catch this exception and print 'Caught an oops'.
print("4.11 Define an exception called OopsException. Raise this exception to see what "
      "happens. Then write the code to catch this exception and print 'Caught an oops'.")


class OopsException(Exception):
    pass


try:
    raise OopsException('ono')
except OopsException as exc:
    print(f"Caught an oops: {exc}")
print()

# 4.12 Use zip() to make a dictionary called movies that pairs these lists: titles =
# ['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a mon
# ster', 'A haunted yarn shop'].
print("4.12 Use zip() to make a dictionary called movies that pairs these lists: titles and plots")
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

zipped = dict(zip(titles, plots))

print(f"Here is the list: {zipped}")
