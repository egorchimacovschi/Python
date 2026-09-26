#exception = an event that interrupts the flow of a program

#1/0 ZeroDivisionError
#1 + '1' Type Error
#int("pizza") ValueError

#if dangerous code we need to check
try:
    number = int(input("Enter a number: "))
    print(10/number)
#control the casses
except ZeroDivisionError:
    print("You cant devide by 0")
except ValueError:
    print("You need to introduce the number")
# final code will be executed even if the exception happend
finally:
    #example closed the opened file
    print("Do some clean up here") 

# or except Exception:
#        print("Something went wrong")