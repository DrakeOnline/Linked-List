# |========================================================|
# |    Title:      main.py                                 |
# |    Author:     Drake G. Cummings                       |
# |    Purpose:    Driver file for Linked List             |
# |    Date:       February 19th, 2021                     |
# |========================================================|

# Imports
from LinkedList import LinkedList

# For printing
divider = "_________________________________"

# Driver code
print()
print(divider)

print("print test:")
test = LinkedList(7)
print(test)

print(divider)
print()

# append_left test
print("append_left test:")
test.append_left(41)
print(test)

print(divider)
print()

# append_right test
print("append_right test:")
test.append_right(24)
test.append_right(19)
test.append_right(20)
print(test)

print(divider)
print()

# pop_left test
print("pop_left test:")
test.pop_left()
print(test)

print(divider)
print()

# pop_right test
print("pop_right test:")
test.pop_right()
print(test)

print(divider)
print()


# contains test
print(test)
print(f"contains 7: {test.contains(7)}")
print(f"contains 999: {test.contains(999)}")

print(divider)
print()


# reverse test
print(test)
print("After reverse")
test.reverse()
print(test)

print(divider)
print()


# Tortiose and Hare test
print("Tortiose and Hare")
print("Test without pattern")
print(test)
test.tortoise_and_hare()
print()
print("Test with pattern")
test.append_right(8)
test.append_right(1)
test.append_right(6)
test.append_right(8)
test.append_right(1)
test.append_right(6)
test.append_right(8)
test.append_right(1)
test.append_right(6)
test.append_right(8)
test.append_right(1)
test.append_right(6)
print(test)
test.tortoise_and_hare()

print(divider)
print()


# Circular test
print("Test if circular")
print("Test on linear")
test.is_circular()
print()
print("Test on circle")
test.make_circular()
test.is_circular()

print(divider)
print()


# In order to make linear again
test = LinkedList(7)
test.append_right(8)
test.append_right(1)
test.append_right(6)
test.append_right(8)
test.append_right(1)
test.append_right(6)
test.append_right(8)
test.append_right(1)
print()

# Lollipop test
print("Test if Lollipop")
print("Test on linear")
test.is_lollipop()
print()
print("Test on lollipop")
# Make lollipop
test.get_tail().next = test.head.next.next.next
test.is_lollipop()

print(divider)
print()
