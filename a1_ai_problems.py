# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

print('hello world')    

#Assigning variables then calling them  
name = 'roger'
name2 = 'Sam'
name3 = 'Alex'
print(name)
print(name2)
print(name3)  


# Count from 1 to 10
for number in range(1, 11):
    print(number)

    #Word Count 
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)

print(f"The number of words in the sentence is: {word_count}")


#Odd or Even 
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

 #Muliplication calculator
num1, num2 = map(float, input("Enter two numbers: ").split())
print(f"Product: {num1 * num2}")











