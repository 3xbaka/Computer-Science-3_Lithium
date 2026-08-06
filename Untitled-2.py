print("Hello! This is the even only dividor! Only even numbers!")
num1 = int(input("Please input the number that you'd like to be divided! Remember, only EVEN numbers!"))
if num1 //2:
    num2 = int(input("Alright! That's an even number! Now, give the number that you'd like it to be divided by."))
else:
    print("Run the code again. That is not an even number")

if num2//2:
    quotient = num1/num2
    print(quotient)
else:
    print("Wrong! That was not an even number. Please run the code again.")