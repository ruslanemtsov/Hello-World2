# Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# Using the range() function:
for x in range(6):
  print(x)

# Using the start parameter:
for x in range(2, 6):
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    print("Banana detected")
    continue
  print(x)

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break