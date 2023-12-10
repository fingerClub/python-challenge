# python-challenge
The following were referenced from ChatGPT:

#For writting new lines of txt
with open('example.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.\n")

#For finding unique candidates

numbers = [1, 2, 3, 4, 5]
    if 6 not in numbers:
        print("6 is not in the list, adding it now.")
        numbers.append(6)
    print(numbers)
