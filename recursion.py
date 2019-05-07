
def main():
    while True:
        try:
            print "What would you like to do?"
            print "1 - Fib"
            print "2 - String Compare"
            print "3 - GCD"
            print "4 - Quit"
            user_input = int(input("Please enter 1 - 3: "))
        except (SyntaxError, NameError) as exception:
            print('\nYou have not entered a number.\n')
            continue
        else:
            break


    if user_input == 1:
        print fibonacci( int(input("Enter Fib: ")) )
    elif user_input == 2:
        print toCompare( raw_input("String 1:") , raw_input("String 2:") )
    elif user_input == 3:
        print gcd( int(input("Enter Int A: ")) , int(input("Enter Int B: ")) )
    elif user_input == 4:
        print('Ok bye.')
    else:
        print('Make a valid selection\n')
        main()


def fibonacci(n):
    if n<0:
        print("Cant be negative")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def toCompare(s1=None,s2=None):
    s1 = list(s1)
    s2 = list(s2)

    if s1 and s2:
        l1 = s1.pop(0)
        l2 = s2.pop(0)

        if (l1 == l2):
            return toCompare(s1,s2)
        elif (l1 < l2):
            return "string 1 < string 2"
        elif (l1 > l2):
            return "string 1 > string 2"

    elif not s1 and s2:
        return "string 1 < string 2"

    elif s1 and not s2:
        return "string 1 > string 2"

    elif not s1 and not s2:
        return "string 1 == string 2"


def gcd(a,b):
    r = max(a,b) % min(a,b)
    if r:
        gcd(min(a,b),r)
    else:
        print "gcd =",b

# Run main if file direcrly executed
if __name__ == '__main__':
    main()
