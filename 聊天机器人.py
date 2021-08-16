print('Hello! My name is Jerry.')
print('I was created in 2021.')
print('Please, remind me your name.')
your_name=input()  # reading a name
print('What a great name you have,'+your_name+"!")
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')
remainder3=int(input())
remainder5=int(input())
remainder7=int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is"+" "+str(age)+"; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')
num_ber=int(input())
n=0
while n<=num_ber:
    print(str(n)+"!")
    n+=1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print('2. To decompose a program into several small subroutines.')
    print('3. To determine the execution time of a program.')
    print("4. To interrupt the execution of a program.")
    while True:
        if int(input())==2:
            print('Completed, have a nice day!')
            break
        else:
            print("Please, try again.")

def end():
    print('Congratulations, have a nice day!')
test()
end()

