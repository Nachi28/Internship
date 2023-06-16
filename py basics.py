# # first python code
# print("nachiket")

# print(" o")
# print("\|/")
# print(" | ")
# print("/ \ ")


# print("hi " * 10)

# price = 10
# rating = 4.9
# name = "Nachi"
# is_published = True
# print(price)

# name = input('What is your name? ')
# color = input("write your fav color")
# print('Hi i am' + name + ",my fav color is " + color, end=" bye")
# Unicode => https://unicode.org/emoji/charts/emoji-list.html
# print("\U0001F600")

# birth_year = input("Birth year: ")
# print (type (birth_year))
# age = 2019 - int(birth_year)
# print(type(age))
# print(age)

# Ascii (65-90 => A - Z)
# print(chr(65))

# strings

# a = [1, 5, 7, 8]
# x, y, z, u = a

# print(x, y, z)

# course = """
# Hello ji
# I am Bantu
# kaise ho
# """
# print(course)

# a="hello"
# print(a[0])
# print(a[-1])

# formated strings
# name="nachi"
# print('Hello, %s' % name)

# txt1 = "My name is {fname}, I'm {age}".format(fname = name, age = 21)
# txt2 = "My name is {0}, I'm {1}".format(name,21)
# txt3 = "My name is {}, I'm {}".format(name,21)

# txt = "For only {price:.2f} rupees!"
# print(txt.format(price = 496))

# name = "Nachi"
# msg = f"hi {name} "
# msg = "hi %s", {name}
# print(msg)

# course= 'Python for Beginners'
# course = len ()
# course.upper()
# course.lower()
# course.capitalize()
# course.find()
# course.replace()
# "..." in course

# strip(): Removes leading and trailing whitespace characters from the string.
# my_string = "   hello world   "
# result = my_string.strip()
# print(result)  # Output: "hello world"

# split(sep): Splits the string into a list of substrings based on a specified separator.
# my_string = "apple,banana,orange"
# result = my_string.split(",")
# print(result)  # Output: ["apple", "banana", "orange"]

# join(iterable): Joins the elements of an iterable (e.g., a list) into a single string using the string as a separator.
# my_list = ["apple", "banana", "orange"]
# result = ",".join(my_list)
# print(result)  # Output: "apple,banana,orange"

# round(number, digits)


# import math
# math.sqrt(x)
# math.factorial(n)
# math.log(num, base)
# math.ceil(4.1)
# math.floor(4.9)
# math.pow(2, 3)
# math.sin(angle)


# list tuple set from website

# # append(element)
# my_list = [1, 2, 3]
# my_list.append(4)

# # extend(iterable)
# my_list = [1, 2, 3]
# my_list.extend([4, 5])

# # insert(index, element)
# my_list = [1, 2, 3]
# my_list.insert(1, 5)

# # remove(element)
# my_list = [1, 2, 3, 2]
# my_list.remove(2)

# # pop(index)
# my_list = [1, 2, 3]
# element = my_list.pop(1)
# print(element)  # Output: 2
# print(my_list)  # Output: [1, 3]

# # index(element)
# my_list = [1, 2, 3, 2]
# index = my_list.index(2)
# print(index)  # Output: 1

# # count(element)
# my_list = [1, 2, 3, 2]
# count = my_list.count(2)
# print(count)  # Output: 2

# # sort()
# my_list = [3, 1, 2]
# my_list.sort()
# print(my_list)  # Output: [1, 2, 3]

# # reverse()
# my_list = [1, 2, 3]
# my_list.reverse()
# print(my_list)  # Output: [3, 2, 1]

# [1, 2, 4, 3]
# li[1:3]   # Return list from index 1 to 3 => [2, 4]
# li[2:]    # Return list starting from index 2 => [4, 3]
# li[:3]    # Return list from beginning until index 3  => [1, 2, 4]
# li[::2]   # Return list selecting every second entry => [1, 4]
# li[::-1]  # Return list in reverse order => [3, 4, 2, 1]
